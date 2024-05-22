function Cargar() {
    fetch('https://mindicador.cl/api')
        .then(Response => Response.json())
        .then(data => {
            const usdValue = data.dolar.valor;
            document.querySelectorAll(".precio").forEach((p)=>{
                console.log(p.innerHTML);
                let precio = parseInt(p.innerHTML.replace("$","").replace(".",""));
                p.innerHTML = `(USD $${(precio / usdValue).toFixed(2)})`;
            });
            //document.querySelector('.precio').innerText = `(USD $${(150000 / usdValue).toFixed(2)})`;


        })

        .catch(Error => console.error('Error fetching data:', Error));

}