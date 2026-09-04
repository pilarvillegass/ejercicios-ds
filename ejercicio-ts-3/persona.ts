interface Persona {
    nombre: string;
    edad: number;
}

const pilar: Persona = {
    nombre: "pilar",
    edad: 22
};

console.log(`nombre: ${pilar.nombre}`);
console.log(`edad: ${pilar.edad}`);