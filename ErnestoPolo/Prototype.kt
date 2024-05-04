class File(var name: String, var content: String): Prototype {
    override fun clone(): File {
        return File(name, content)
    }
}

fun main() {
<<<<<<< HEAD
=======
    // el usuario tiene el texto "pantalones" copiado en el portapapeles del celular
>>>>>>> 27bef2c5b7a861948d98713bfc6406d2ff6394a9
    var file = File("archivo.txt", "lorem ipsum ...")
    var file2 = file.clone()
    file2.name = "otroArchivo.text"

    println(file.nombre)
    println(file2.nombre)
}
