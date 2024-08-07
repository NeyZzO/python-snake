import json, os, datetime


class ScoreHandler:
    FILE_PATH = './score.json'

    @staticmethod
    def saveScore(score: int) -> bool:
        best: int = ScoreHandler.loadScore()
        if score > best:
            with open(ScoreHandler.FILE_PATH, 'w') as file:
                obj = {"best": score, "date": datetime.datetime.now().isoformat()}
                json.dump(obj, file)
            return True
        return False
        # Si l'attr score > best, alors tu complète le fichier json et renvoyer True pour indiquer un nouveau meilleur score, sinon tu fais rien et renvoie False

    @staticmethod
    def loadScore() -> int:
        # Charger le fichier json, le lire et renvoyer le meilleur score
        if not os.path.exists(ScoreHandler.FILE_PATH):
            with open('./score.json', 'w') as file: 
                obj = {"best": 0, "date": datetime.datetime.now().isoformat()}
                json.dump(obj, file)
            return 0
        
        with open(ScoreHandler.FILE_PATH, 'r') as file:
            data = json.load(file)
            print(data)
            return data.get('best', 0)

if __name__ == "__main__":
    ScoreHandler.loadScore()