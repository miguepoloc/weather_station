import Foundation

//MARK: Creacion de un factory
protocol Shape {
    func draw()
}


// Clase para representar un círculo
class Circle: Shape {
    func draw() {
        print("Drawing Circle")
    }
}

// Clase para representar un cuadrado
class Square: Shape {
    func draw() {
        print("Drawing Square")
    }
}

enum ShapeType{
    case circle, square
}

class ShapeFactory {
    func createShape(shapeType: ShapeType) -> Shape? {
        switch shapeType {
        case .circle:
            return Circle()
        case .square:
            return Square()
        default:
            print("Unsupported shape type")
            return nil
        }
    }
}

let factory = ShapeFactory()

if let circle = factory.createShape(shapeType: .circle) {
    circle.draw() // Output: Drawing Circle
}

if let square = factory.createShape(shapeType: .square) {
    square.draw() // Output: Drawing Square
}
