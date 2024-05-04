//// Singleton
class Singleton private constructor() {

    companion object {

        @Volatile private var instance: Singleton? = null

        fun getInstance() =
            instance ?: synchronized(this) {
                instance ?: Singleton().also { instance = it }
            }
    }
}

// Strategy
data class Libro(val titulo: String, val precio: Double)
data class Cliente(val nombre: String, val tipoMembresia: TipoMembresia)

enum class TipoMembresia {
    REGULAR, PREMIUM
}

class CalculadoraDescuento {
    fun calcularDescuento(libro: Libro, cliente: Cliente): Double {
        return if (cliente.tipoMembresia == TipoMembresia.REGULAR) {
            libro.precio * 0.1
        } else {
            libro.precio * 0.2
        }
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

class CalculadoraDescuento(private val estrategiaDescuento: EstrategiaDescuento) {
    fun calcularDescuento(libro: Libro): Double {
        return estrategiaDescuento.calcularDescuento(libro)
    }
}

class PruebaCalculadoraDescuento {

    private fun crearCalculadoraDescuento(cliente: Cliente): CalculadoraDescuento {
        val estrategiaDescuento = when (cliente.tipoMembresia) {
            TipoMembresia.REGULAR -> EstrategiaDescuentoClienteRegular()
            TipoMembresia.PREMIUM -> EstrategiaDescuentoClientePremium()
        }

        return CalculadoraDescuento(estrategiaDescuento)
    }

}


// Factory

class FabricaValidadores {

    fun obtenerValidador(documentoUsuario: String?): ValidadorDocumento? =

         when {
            esDNI(documentoUsuario) ->  ValidadorDNI(documentoUsuario)
            esNIE(documentoUsuario) ->  ValidadorNIE(documentoUsuario)
            else -> null
        }

    // Se necesita implementar la lógica
    private fun esDNI(documentoUsuario: String?) = true

    // Se necesita implementar la lógica
    private fun esNIE(documentoUsuario: String?) = false
}

interface ValidadorDocumento {

    fun validar(): Boolean
}

class ValidadorNIE(documentoUsuario: String?): ValidadorDocumento {

    // Se necesita implementar la lógica
    override fun validar() = true
}

class ValidadorDNI(documentoUsuario: String?): ValidadorDocumento {

    // Se necesita implementar la lógica
    override fun validar() = true
}


fun main() {

    /////////////////////////////////////////////
    ///// Singleton /////////////////////////////
    /////////////////////////////////////////////

    // Primera instancia
    var mySingleton = Singleton.getInstance()

    // La misma instancia que la variable mySingleton
    var mySecondSingleton = Singleton.getInstance()

    // Error debes usar el metodo getInstance para asegurar el correcto funcionamiento del singleton
    var myThirdSingleton = Singleton()

    //////////////////////////////////////////////
    //// Strategy ////////////////////////////////
    //////////////////////////////////////////////

    // Para un consumidor regular
    var libro = Libro("ser pupular en 10 dias", 100.0)
    var cliente = Cliente("Juan Pérez", TipoMembresia.REGULAR)
    var calculadoraDescuento = crearCalculadoraDescuento(cliente)
    var descuento = calculadoraDescuento.calcularDescuento(libro)

    println("esperado : 10.0" + " --- Actual: " + descuento)

    // Para un consumidor premium
    libro = Libro("como ser millonario", 100.0)
    cliente = Cliente("Jhon gutierrez", TipoMembresia.REGULAR)
    calculadoraDescuento = crearCalculadoraDescuento(cliente)
    descuento = calculadoraDescuento.calcularDescuento(libro)
    println("esperado : 20.0" + " --- Actual: " + descuento)

    //////////////////////////////////////////////
    //// Factory  ////////////////////////////////
    //////////////////////////////////////////////

    val validator = FabricaValidadores().obtenerValidador("00000000F")
    if (validator?.validar() == true) {
        Log.i(TAG, "The document is correct")
    } else {
        Log.i(TAG, "The document is not correct")
    }
}