import Foundation
//
//Proporciona una forma de evaluar lenguajes o expresiones gramaticales. Ejemplo: Crear un intérprete de expresiones matemáticas para evaluar fórmulas.
//

//MARK: Creacion de un interpreter
protocol Expression {
    func interpret() -> Int
}

// Clase para expresiones numéricas
class Number: Expression {
    private var value: Int
    
    init(_ value: Int) {
        self.value = value
    }
    
    func interpret() -> Int {
        return value
    }
}

// Clase para expresiones de suma
class Add: Expression {
    private var left: Expression
    private var right: Expression
    
    init(_ left: Expression, _ right: Expression) {
        self.left = left
        self.right = right
    }
    
    func interpret() -> Int {
        return left.interpret() + right.interpret()
    }
}

// Ejemplo de uso del patrón Interpreter
let expression = Add(Number(5), Add(Number(3), Number(2)))
let result = expression.interpret() // Resultado será 10 (5 + (3 + 2))
print("El resultado de la expresión es: \(result)")
