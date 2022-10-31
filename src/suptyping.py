class Car:
    pass

class RaceCar(Car):
    pass

# В данном случае ремонт расчитан на абстрактную машину и можем подставить как Car так и RaceCar,
# поэтому тут случай ковариантности 
class RepairService:

    def repair(car: Car):
        some_operations_on_abstract_car(car)

# тут происходит ремонт конкретной гоночной машины, а как известна не все машины гоночные, поэтому 
# подставить тут общий случай Car нельзя, только вернувшись к родителю, следует случай контравариантности
class RepairRaceCarService(RepairService):

    def repair(race_car: RaceCar):
        some_operations_on_concrete_car(race_car)




