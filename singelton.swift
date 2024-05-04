import Foundation

//MARK: Creacion de un singleton
 class Singleton {
    static let sharedInstance = Singleton()
    var param1: String?
    var param2: String?
    
    private init(){
        param1 = nil
        param2 = nil
    }
    
     func setParams(_ param1: String, _ param2: String){
         self.param1 = param1
         self.param2 = param2
     }
}

//uso de singleton
Singleton.sharedInstance.setParams("juan", "bernier")
print(Singleton.sharedInstance.param1)


