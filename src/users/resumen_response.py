from pydantic import BaseModel
class resumen_response:
    def __init__(self,N_empleados:int, salario_total:float, promedio:float) -> None:
        self.N_empleados=N_empleados
        self.salario_total=salario_total
        self.promedio=promedio

class ResumenResponse(BaseModel):
    N_empleados: int
    salario_total: float
    promedio: float