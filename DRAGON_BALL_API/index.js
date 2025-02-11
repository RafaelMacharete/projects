// https://dragonball-api.com/api/characters

async function fetchData() {
    let requisition = await fetch('https://dragonball-api.com/api/characters?limit=58');
    let json = await requisition.json();
    
    console.log(json.items);

    
    let card = document.querySelector('.card')
    let h1Name = document.querySelector('#name');
    let charImage = document.querySelector('#image')

    let section = document.querySelector('section');

    for (const element of json.items) {
        let divCard = document.createElement('div');
        divCard.classList.add('card')
        
        let nameElement = document.createElement('h1');
        nameElement.innerHTML = element.name;

        let imageElement = document.createElement('img')
        imageElement.src = element.image

        section.appendChild(divCard)
        divCard.appendChild(nameElement);
        divCard.appendChild(imageElement);
    }

}

fetchData();