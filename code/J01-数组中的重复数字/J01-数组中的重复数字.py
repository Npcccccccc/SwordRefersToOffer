class Solution:
    def duplicate(self, numbers:list, length:int)->bool:
        if not numbers:
            return False

        for i in range(length):
            if numbers[i] < 0 or numbers[i] > length - 1:
                return False
        
        for i in range(length):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    self.duplication = numbers[i]
                    return True
                
                numbers[i], numbers[numbers[i]] = numbers[numbers[i]], numbers[i]
        return False

    def get_duplication(self)->int:
        return self.duplication