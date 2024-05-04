class File(var name: String, var content: String): Prototype {
    override fun clone(): File {
        return File(name, content)
    }
}

fun main() {
    var file = File("archivo.txt", "lorem ipsum ...")
    var file2 = file.clone()
    file2.name = "otroArchivo.text"

    println(file.nombre)
    println(file2.nombre)
}
