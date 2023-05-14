from dataclasses import dataclass

@dataclass(repr=True, init=True)
class Serie:
    '''
        Series para plotar o gráfico echart
    '''
    name: str
    type: str
    stack: str
    data: list

    def to_dict(self):
        return {
            'name': self.name,
            'type': self.type,
            'stack': self.stack,
            'data': self.data
        }