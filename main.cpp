#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


class Animal {
private:
    string name;
    string species;
    string animalID;
    bool adopted;

public:
    static int totalAnimals;

    Animal(const string& Name, const string& Species, const string& Id){
        name = Name;
        species = Species;
        animalID = Id;
        adopted = false;
        ++totalAnimals;
    }

     ~Animal() {
        --totalAnimals;
    }

    void displayInfo() const {
        cout << "Name: " << name
             << ", Species: " << species
             << ", ID: " << animalID
             << ", Adopted: " << (adopted ? "Yes" : "No")
             << '\n';
    }

    void setAdoptionStatus(bool status) {
        adopted = status;
    }

    string getSpecies() const {
        return species;
    }

    bool isAdopted() const {
        return adopted;
    }

    string getName() const {
        return name;
    }
    string getID() const {
        return animalID;
    }

    static int getTotalAnimals() {
        return totalAnimals;
    }
};

int Animal::totalAnimals = 0;


class ShelterUser {
protected:
    string name;
    int userID;
public:
    ShelterUser(const string& Name, int Id) {
        name = Name;
        userID = Id;
    }
    virtual ~ShelterUser() {}

    virtual void displayUserInfo() const = 0;

    string getName() const {
        return name;
    }
    int getUserID() const {
        return userID;
    }
};


class Adopter : public ShelterUser {
private:
    vector<Animal*> adoptedPets;
public:
    Adopter(const string& name, int id) : ShelterUser(name, id) {}

    ~Adopter() override =default;

    void displayUserInfo() const override {
        cout << "Adopter: " << name << ", ID: " << userID << '\n';
        if (!adoptedPets.empty()) {
            cout << "  Adopted pets:\n";
            for (const auto &a : adoptedPets) {
                if (a) {
                    cout << "    - " << a->getName() << " (" << a->getID() << ")\n";
                }
            }
        }
    }

    bool adoptPet(Animal* a) {
        if (!a) {
            return false;
        }
        if (a->isAdopted()) {
            cout << "Error: '" << a->getName() << "' (" << a->getID() << ") is already adopted.\n";
            return false;
        }
        a->setAdoptionStatus(true);
        adoptedPets.push_back(a);

        cout << "Adopter " << name << " is adopting \"" << a->getName() << "\"." << '\n';
        return true;
    }

    bool returnPet(Animal* a) {
        if (!a) {
            return false;
        }
        auto it = find(adoptedPets.begin(), adoptedPets.end(), a);
        if (it == adoptedPets.end()) {
            cout << "Error: " << name << " has not adopted \"" << a->getName() << "\"." << '\n';
            return false;
        }
        a->setAdoptionStatus(false);
        adoptedPets.erase(it);

        cout << "Adopter " << name << " returned \"" << a->getName() << "\"." << '\n';
        return true;
    }

    bool hasAdopted(Animal* a) const {
        return find(adoptedPets.begin(), adoptedPets.end(), a) != adoptedPets.end();
    }
};

class ShelterStaff : public ShelterUser {
public:
    ShelterStaff(const string& name, int id) : ShelterUser(name, id) {}
    ~ShelterStaff() override = default;

    void displayUserInfo() const override {
        cout << "Staff: " << name << ", ID: " << userID << '\n';
    }

    void addAnimal(class ShelterSystem& system, Animal* a);

    void removeAnimal(class ShelterSystem& system, const string& animalID);
};


class ShelterSystem {
private:
    vector<Animal*> animals;
    vector<ShelterUser*> users;


    Animal* searchAnimalRecursive(const string& name, size_t index) const {
        if (index >= animals.size()) {
            return nullptr;
        }
        if (animals[index] && animals[index]->getName() == name) {
            return animals[index];
        }
        return searchAnimalRecursive(name, index + 1);
    }

public:
    ShelterSystem() {}

    ~ShelterSystem() {

        for (auto a : animals) {
            delete a;
        }
        animals.clear();

        for (auto u : users) {
            delete u;
        }
        users.clear();
    }

    void addUser(ShelterUser* u) {
        if (!u) {
            return;
        }
        users.push_back(u);
        if (dynamic_cast<Adopter*>(u)) {
            cout << "Adding new adopter: " << u->getName() << " (ID: " << u->getUserID() << ")\n";
        }else{
            cout << "Adding new staff: " << u->getName() << " (ID: " << u->getUserID() << ")\n";
        }
    }


    void addAnimal(Animal* a) {
        if (!a) {
            return;
        }
        animals.push_back(a);
        cout << "Adding animal: \"" << a->getName() <<"\""<< " ("<<a->getSpecies()<<")"<<", ID: " << a->getID() << '\n';
        cout << "Total animals: " << Animal::getTotalAnimals() << '\n';
    }

    bool removeAnimal(const string& animalID) {
        for (size_t i = 0; i < animals.size(); ++i) {
            if (animals[i] && animals[i]->getID() == animalID) {
                if (animals[i]->isAdopted()) {
                    cout << "Warning: removing an adopted animal (" << animals[i]->getName() << ").\n";
                }
                delete animals[i];
                animals.erase(animals.begin() + i);
                cout << "Animal with ID " << animalID << " removed from shelter.\n";
                cout << "Total animals: " << Animal::getTotalAnimals() << '\n';
                return true;
            }
        }
        cout << "Error: No animal with ID " << animalID << " found.\n";
        return false;
    }

    Animal* searchAnimal(const string& name) const {
        return searchAnimalRecursive(name, 0);
    }

    void displayAllAnimals() const {
        cout << "Displaying all animals:\n";
        for (const auto &a : animals) {
            if (a) {
                a->displayInfo();
            }
        }
        cout << "Total animals: " << Animal::getTotalAnimals() << '\n';
    }

    void displayAllUsers() const {
        cout << "Displaying all users:\n";
        for (const auto& u : users) {
            if (u) u->displayUserInfo();
        }
    }


    Animal* getAnimalByID(const string& id) const {
        for (auto a : animals) if (a && a->getID() == id) return a;
        return nullptr;
    }
};


void ShelterStaff::addAnimal(ShelterSystem& system, Animal* a) {
    system.addAnimal(a);
}

void ShelterStaff::removeAnimal(ShelterSystem& system, const string& animalID) {
    system.removeAnimal(animalID);
}


int main() {
    cout << "Animal Shelter System Initialized." << '\n';

    ShelterSystem* system = new ShelterSystem();


    Adopter* adopterJohn = new Adopter("John Doe", 101);
    ShelterStaff* staffSarah = new ShelterStaff("Sarah Smith", 102);

    system->addUser(adopterJohn);
    system->addUser(staffSarah);

    cout<<"\n\n";


    Animal* buddy = new Animal("Buddy", "Dog", "D101");
    staffSarah->addAnimal(*system, buddy);

    Animal* whiskers = new Animal("Whiskers", "Cat", "C102");
    staffSarah->addAnimal(*system, whiskers);

    cout<<"\n\n";


    adopterJohn->adoptPet(buddy);

    adopterJohn->returnPet(buddy);

    cout<<"\n\n";


    system->displayAllAnimals();
    system->displayAllUsers();


    delete system;

    return 0;
}

