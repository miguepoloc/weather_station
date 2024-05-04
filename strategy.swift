import Foundation

//MARK: Creacion de un Strategy
protocol Operation {
    func execute(_ num1: Double, _ num2: Double) -> Double
}

// Clase para la suma
class AdditionOperation: Operation {
    func execute(_ num1: Double, _ num2: Double) -> Double {
        return num1 + num2
    }
}

// Clase para la resta
class SubtractionOperation: Operation {
    func execute(_ num1: Double, _ num2: Double) -> Double {
        return num1 - num2
    }
}

// Clase para la multiplicación
class MultiplicationOperation: Operation {
    func execute(_ num1: Double, _ num2: Double) -> Double {
        return num1 * num2
    }
}

// Clase para la división
class DivisionOperation: Operation {
    func execute(_ num1: Double, _ num2: Double) -> Double {
        guard num2 != 0 else {
            fatalError("Error: Division by zero")
        }
        return num1 / num2
    }
}

class Calculator {
    private var operation: Operation
    
    init(operation: Operation) {
        self.operation = operation
    }
    
    func setOperation(_ operation: Operation) {
        self.operation = operation
    }
    
    func calculate(_ num1: Double, _ num2: Double) -> Double {
        return operation.execute(num1, num2)
    }
}

// Uso de la calculadora
let calculator = Calculator(operation: AdditionOperation())
print(calculator.calculate(5, 3)) // Output: 8.0

calculator.setOperation(SubtractionOperation())
print(calculator.calculate(5, 3)) // Output: 2.0
