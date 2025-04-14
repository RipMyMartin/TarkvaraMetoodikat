var nameList = [
    'Time', 'Fly', 'Fall', 'Green', 'Kitty', 'Fear', 'Mine', 'Game', 'Gun', 'Script', 'Geo',
    'Extreme','niverse','Ultimate','Death','Ready','Monkey','Elevator','Wrench','Grease',
    'Head','Theme','Grand','Cool','Kid','Boy','Girl','Vortex','Paradox'
];

class Platform {
    constructor(resources) {
        this.resources = resources;
    }
    consume(amount){
        this.resources -= amount;
    }
}

class Floor {
    constructor(lvl, peopleCount) {
        this.lvl = lvl;
        this.peopleCount = peopleCount;
    }
    processPlatform(platform){
        console.log("Korrus: ", this.lvl);
        this.peopleCount.forEach((person) => {
            person.makeDecision(platform);
        });
        console.log("resurside jääk", platform.resources);
    }
}

class Person {
    constructor(name, pepercent) {
        this.name = name;
        this.pepercent = pepercent;
    }

    makeDecision(platform) {
        let chance = Math.random() * 100;
        if (chance < this.pepercent && platform.resources > 0) {
            const eatAmount = 10;
            platform.consume(eatAmount);
            console.log(this.name, "Sõi: ", eatAmount,"toitu" );
        }
    }
}

let floors = [];

for(let i = 0; i < 10; i++) {
    let Person1 = new Person(
        nameList[Math.floor(Math.random() * nameList.length)],
        Math.floor(Math.random() * 100 ) + 1
    );
    let Person2 = new Person(
        nameList[Math.floor(Math.random() * nameList.length)],
        Math.floor(Math.random() * 100 ) + 1
    );

    let floor = new Floor(i, [Person1, Person2]);
    floors.push(floor);
}

console.log(floors);

let platform = new Platform(100);

floors.forEach((floor) => {
    floor.processPlatform(platform);
});