import math
class Material:
    def __init__(self, name, amount, cost_dict):
        self.name = name
        self.amount = amount
        self.recipe = cost_dict
    
    def __str__(self):
        return self.name+": "+str(self.recipe)
    
    def __repr__(self):
        return self.name+": "+str(self.recipe)

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
        total_crafts = {}
        remainders = {}
        total_cost = {}
        craft_queue = []
        for item in self.targets:
            curr_total = self.targets[item]
            item_obj = self.registered_res[item]
            num_crafts = self.calc_crafts(item, curr_total, remainders)
            if num_crafts == 0:
                continue
            
            if item not in total_crafts:
                total_crafts[item] = 0
            total_crafts[item] += num_crafts
            # This function updates remainders
            
            for component in item_obj.recipe:
                if component not in craft_queue:
                    craft_queue.append(component)
                if component not in total_cost:
                    total_cost[component] = 0
                total_cost[component] += num_crafts*item_obj.recipe[component]
        
        return total_cost  

    def calc_crafts(self, item, target_total, remainders):
        rec_yield = self.registered_res[item].amount
        if target_total % rec_yield == 0:
            return target_total / rec_yield
        else:
            #Now, the fun begins
            if item not in remainders:
                remainders[item] = 0
            if remainders[item] <= target_total % rec_yield:
                remainders[item] -= target_total % rec_yield
                return target_total // rec_yield
            else:
                overflow = target_total % rec_yield - remainders[item]
                
                
        
def test1():
    circuit_mat = {"Plastic_Board":1, "Thin_Red_A_Wire":4, "SMD_Cap":4, "Coil":4, "MV_Circuit3":2, "RAM_Chip": 4}
    dummy1 = Material("HV_Circuit2", 1, circuit_mat)
    circuit_mat = {"Plastic_Board":1, "Thin_Red_A_Wire":4, "SMD_Cap":4, "SMD_Res":4,"SMD_Transistor":4, "CPU_Chip":1}
    dummy2 = Material("MV_Circuit3", 1, circuit_mat)
    
    print(dummy1)
    print(dummy2)
    
    HV_Circuit = RecipeChain()
    HV_Circuit.add_target(dummy1.name)
    HV_Circuit.register_res(dummy1)
    print(HV_Circuit.calculate_total())
    HV_Circuit.register_res(dummy2)
    print(HV_Circuit.calculate_total())


def test2():
    circuit_mat = {"Plastic_Board":1, "sillycon":400, "Thin_Red_A_Wire":4}
    dummy1 = Material("HV_Circuit2", 3, circuit_mat)
    HV_Circuit = RecipeChain()
    HV_Circuit.add_target(dummy1.name)
    HV_Circuit.register_res(dummy1)
    residual = {}
    
    
    
if __name__ == "__main__":
    test1()
    