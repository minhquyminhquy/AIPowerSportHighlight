import json
from typing import Dict, List, Optional

class DataManager:
    def __init__(self, data_path: str = "data/"):
        self.data_path = data_path
        self.matches: Dict = {}
        self.players: Dict = {}
        self.events: Dict = {}
        self.load_data()
    
    def load_data(self):
        """Load data from JSON files"""
        try:
            with open(f"{self.data_path}matches.json", "r") as f:
                self.matches = json.load(f)
            with open(f"{self.data_path}players.json", "r") as f:
                self.players = json.load(f)
            with open(f"{self.data_path}events.json", "r") as f:
                self.events = json.load(f)
        except FileNotFoundError:
            # Initialize empty data files if they don't exist
            self.save_data()
    
    def save_data(self):
        """Save data to JSON files"""
        with open(f"{self.data_path}matches.json", "w") as f:
            json.dump(self.matches, f)
        with open(f"{self.data_path}players.json", "w") as f:
            json.dump(self.players, f)
        with open(f"{self.data_path}events.json", "w") as f:
            json.dump(self.events, f)
    
    def add_match(self, match_data: Dict):
        """Add a new match"""
        match_id = str(len(self.matches) + 1)
        self.matches[match_id] = match_data
        self.save_data()
        return match_id
    
    def add_event(self, event_data: Dict):
        """Add a new event"""
        event_id = str(len(self.events) + 1)
        self.events[event_id] = event_data
        self.save_data()
        return event_id
    
    def get_match_events(self, match_id: str, event_type: Optional[str] = None) -> List[Dict]:
        """Get events for a specific match"""
        match_events = [
            event for event in self.events.values()
            if event["match_id"] == match_id
            and (event_type is None or event["type"] == event_type)
        ]
        return match_events
    
    def get_player_events(self, match_id: str, player_id: str) -> List[Dict]:
        """Get events for a specific player in a match"""
        player_events = [
            event for event in self.events.values()
            if event["match_id"] == match_id and event["player_id"] == player_id
        ]
        return player_events