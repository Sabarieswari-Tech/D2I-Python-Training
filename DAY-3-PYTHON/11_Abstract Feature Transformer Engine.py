from abc import ABC,abstractmethod

class BaseDataTransformer(ABC):
    @abstractmethod
    def transform(self,data):
        pass

class NormalizerTransformer(BaseDataTransformer):
    def transform(self,data):
        mn=min(data)
        mx=max(data)
        return [round((x-mn)/(mx-mn),2) for x in data]

class StandardizerTransformer(BaseDataTransformer):
    def transform(self,data):
        mean=sum(data)/len(data)
        std=(sum((x-mean)**2 for x in data)/len(data))**0.5
        return [round((x-mean)/std,2) for x in data]

norm=NormalizerTransformer()
std_t=StandardizerTransformer()

print(norm.transform([10,20,50,100]))
print(std_t.transform([10,20,30,40,50]))