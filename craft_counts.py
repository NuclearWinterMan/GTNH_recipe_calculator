
class Material:
    def __init__(self, name, amount, cost_dict):
        self.name = name
        self.amount = amount
        self.cost = cost_dict
    
    def __str__(self):
        return self.name+": "+str(self.cost)

class RecipeChain:
    def __init__(self):
        self.targets = {}
        self.registered_res = {}
        
    def register_res(self, res):
        if res.name in self.registered_res:
            return
        self.registered_res[res.name] = res

    def add_target(self, target, num=1):
        if target not in self.targets:
            self.targets[target]=0
        self.targets[target] += num

    def calculate_total(self):
        

def test1():
    circuit_mat = {"Plastic_Board":1, "Thin_Red_A_Wire":4, "SMD_Cap":4, "Coil":4, "MV_Circuit":2, "RAM_Chip": 4}
    dummy1 = Material("HV_Circuit2", 1, circuit_mat)
    circuit_mat = {"Plastic_Board":1, "Thin_Red_A_Wire":4, "SMD_Cap":4, "SMD_Res":4,"SMD_Tstor":4, "CPU_Chip":1}
    dummy2 = Material("MV_Circuit", 1, circuit_mat)
    
    print(dummy1)
    print(dummy2)
    
    HV_circuit

if __name__ == "__main__":
    test1()
    