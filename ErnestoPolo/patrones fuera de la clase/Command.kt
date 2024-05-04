interface Command {
    fun execute()
    fun undo()
}

class TextfieldView(var clipBoardCopy: String): Command {
    var text: String = "EMPTY"

    override fun execute() {
        text = clipBoardCopy
    }

    override fun undo() {
        text = "EMPTY"
    }
}

fun main() {
    // el usuario tiene el texto "pantalones" copiado en el portapapeles del celular
    var textfield = TextfieldView("pantalones")
    // el usuario realiza pegar sobre el cuadro de texto
    textfield.execute()
    println(textfield.text)
    // se arrepiente y preciona back en el dispositivo
    textfield.undo()
    println(textfield.text)
}