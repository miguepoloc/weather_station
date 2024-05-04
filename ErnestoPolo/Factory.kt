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
    //////////////////////////////////////////////
    //// Factory  ////////////////////////////////
    //////////////////////////////////////////////
    val validator = FabricaValidadores().obtenerValidador("00000000F")
    if (validator?.validar() == true) {
        println("The document is correct")
    } else {
        println("The document is not correct")
    }
}
