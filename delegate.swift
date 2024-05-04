import Foundation

//MARK: Creacion de un Delegate
protocol SomeDelegate: AnyObject {
    func didReceiveData(data: String)
}

// Clase que necesita un delegado
class SomeClass {
    weak var delegate: SomeDelegate?
    
    func fetchData() {
        // Simular la obtención de datos
        let data = "Datos obtenidos"
        // Notificar al delegado una vez que se obtienen los datos
        delegate?.didReceiveData(data: data)
    }
}

// Clase que actúa como delegado
class DelegateClass: SomeDelegate {
    func didReceiveData(data: String) {
        print("Datos recibidos: \(data)")
    }
}

// Uso del patrón de delegado
let object = SomeClass()
let delegate = DelegateClass()
object.delegate = delegate
object.fetchData() // Esto imprimirá "Datos recibidos: Datos obtenidos"
