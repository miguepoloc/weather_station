class Perro() {
    private var nombre: String = ""
    private var color: String = ""
    private var edad: Int = 0
    private var peso: Double = 0.0
    private var genero: String = ""
    private var raza: String = ""

    class PerroBuilder {
        private var perroInstance = Perro()

        fun withNombre(nombre: String): PerroBuilder {
            perroInstance.nombre = nombre
            return this
        }

        fun withColor(color: String): PerroBuilder {
            perroInstance.color = color
            return this
        }

        fun withEdad(edad: Int): PerroBuilder {
            perroInstance.edad = edad
            return this
        }

        fun withPeso(peso: Double): PerroBuilder {
            perroInstance.peso = peso
            return this
        }

        fun withGenero(genero: String): PerroBuilder {
            perroInstance.genero = genero
            return this
        }

        fun withRaza(raza: String): PerroBuilder {
            perroInstance.raza = raza
            return this
        }

        fun build(): Perro = perroInstance
    }
}

fun main() {
    val kiara = Perro.PerroBuilder()
        .withNombre("Kiara")
        .withColor("Marrón")
        .withEdad(3)
        .withPeso(10.5)
        .withGenero("Hembra")
        .withRaza("Labrador Retriever")
        .build()
    println(kiara.toString())
}