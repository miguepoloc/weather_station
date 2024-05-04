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


fun main() {

    /////////////////////////////////////////////
    ///// Singleton /////////////////////////////
    /////////////////////////////////////////////

    // Primera instancia
    val mySingleton = Singleton.getInstance()

    // La misma instancia que la variable mySingleton
    val mySecondSingleton = Singleton.getInstance()

    println("Hash code: " + mySingleton.hashCode())
    println("Hash code: " + mySecondSingleton.hashCode())

    // Error debes usar el metodo getInstance para asegurar el correcto funcionamiento del singleton
    // var myThirdSingleton = Singleton()
}