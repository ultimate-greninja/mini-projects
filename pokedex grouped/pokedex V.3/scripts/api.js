const btnSearch = document.getElementById("btnSearch");
btnSearch.addEventListener("click",() => {
    let pokemonName = document.getElementById("search").value;
    let url = `https://pokeapi.co/api/v2/pokemon/${pokemonName.toLowerCase()}`;
    fetch(url)
    .then(res =>res.json())
    .then(res =>{
    console.log(res)
    const pokedexNum = document.querySelector("#pokedexNumber")
    pokedexNum.textContent = res.id
    const name = document.querySelector("#name")
    name.textContent = res.name.toUpperCase()
    // const mainImage = document.querySelector("");
    // mainImage.innerHTML = `<img scr="${res.sprites.front}">`
    
    //????
    // const male = document.querySelector("#male");
    // male.innerHTML = `<img scr = "${res.sprites.front_default}">`
    //????
    
    const types = document.querySelector("#types")
    types.innerHTML = `<span></span>`
        for(let index = 0; index < res.types.length;index++) {
            types.innerHTML += ` <span class="${res.types[0].type.name}">${res.types[index].type.name}`.toUpperCase()
    }
    const ability = document.querySelector("#ability")
    ability.innerHTML = `<span></span>`
        for(let index = 0; index < res.abilities.length;index++) {
            ability.innerHTML += ` <span class="${res.abilities[0].ability.name}">${res.abilities[index].ability.name}`.toUpperCase()
    }
    const games = document.querySelector("#games")
    games.innerHTML = `<span></span>`
        for(let index = 0; index < res.game_indices.length;index++) {
            games.innerHTML += ` <span class="${res.game_indices[0].version.name}">${res.game_indices[index].version.name}`.toUpperCase()
    }
})    
})
