// Strategy
data class Libro(val titulo: String, val precio: Double)
data class Cliente(val nombre: String, val tipoMembresia: TipoMembresia)

enum class TipoMembresia {
    REGULAR, PREMIUM
}

class CalculadoraDescuento(private val estrategiaDescuento: EstrategiaDescuento) {
    fun calcularDescuento(libro: Libro): Double {
        return estrategiaDescuento.calcularDescuento(libro)
    }
}

interface EstrategiaDescuento {
    fun calcularDescuento(libro: Libro): Double
}

class EstrategiaDescuentoClienteRegular : EstrategiaDescuento {
    override fun calcularDescuento(libro: Libro): Double {
        return libro.precio * 0.1
    }
}

class EstrategiaDescuentoClientePremium : EstrategiaDescuento {
    override fun calcularDescuento(libro: Libro): Double {
        return libro.precio * 0.2
    }
}

class PruebaCalculadoraDescuento {

    fun crearCalculadoraDescuento(cliente: Cliente): CalculadoraDescuento {
        val estrategiaDescuento = when (cliente.tipoMembresia) {
            TipoMembresia.REGULAR -> EstrategiaDescuentoClienteRegular()
            TipoMembresia.PREMIUM -> EstrategiaDescuentoClientePremium()
        }

        return CalculadoraDescuento(estrategiaDescuento)
    }

}


fun main() {

    //////////////////////////////////////////////
    //// Strategy ////////////////////////////////
    //////////////////////////////////////////////

    // Para un consumidor regular
    var libro = Libro("ser pupular en 10 dias", 100.0)
    var cliente = Cliente("Juan Pérez", TipoMembresia.REGULAR)
    var calculadoraDescuento = PruebaCalculadoraDescuento().crearCalculadoraDescuento(cliente)
    var descuento = calculadoraDescuento.calcularDescuento(libro)

    println("esperado : 10.0 --- Actual: $descuento")

    // Para un consumidor premium
    libro = Libro("como ser millonario", 100.0)
    cliente = Cliente("Jhon gutierrez", TipoMembresia.PREMIUM)
    calculadoraDescuento = PruebaCalculadoraDescuento().crearCalculadoraDescuento(cliente)
    descuento = calculadoraDescuento.calcularDescuento(libro)
    println("esperado : 20.0 --- Actual: $descuento")

}