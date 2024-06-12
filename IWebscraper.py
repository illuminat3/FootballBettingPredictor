from abc import ABC, abstractmethod
from typing import List, Tuple
from team import Team

class IWebscraper(ABC):
    
    @abstractmethod
    def GetGamesSlugs(self) -> List[str]:
        pass
    
    @abstractmethod
    def GetGameOdds(self) -> Tuple['Team', 'Team']:
        pass