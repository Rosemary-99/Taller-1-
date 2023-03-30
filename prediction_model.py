from annoy import AnnoyIndex
import pandas as pd

class PredictionModel:

    def __init__(self):
        self.tracks_df = pd.read_csv("C:\\Users\\ALEJANDRO\\segundoRosemary\\app\\normal_track3.csv")
        self.tracks_df["name"].fillna("", inplace=True)
        self.tracks_df["artists"].fillna("", inplace=True)

        self.artist_df = pd.read_csv("C:\\Users\\ALEJANDRO\\segundoRosemary\\app\\normal_artist.csv")

        features = ["explicit", "danceability", "energy", "loudness", "speechiness", "liveness", "valence"]
        len_features = len(features)
        self.annoy_loaded = AnnoyIndex(len_features, "euclidean")
        self.annoy_loaded.load("C:\\Users\\ALEJANDRO\\segundoRosemary\\app\models\\spotify.ann")

    def make_predictions_artist(self, data):
        predict_tracks_df = self.tracks_df.loc[self.tracks_df["artists"].str.contains(data)]
        predict_tracks_df["release_date"] = pd.to_datetime(predict_tracks_df["release_date"])
        predict_tracks_df = predict_tracks_df.sort_values(by=["release_date"], ascending=False)

        # get the index of the first track
        first_track_index = predict_tracks_df.index[0]

        neighbors = self.annoy_loaded.get_nns_by_item(first_track_index, 10)

        result = self.tracks_df.loc[neighbors]

        track_df_exploded = result.explode("id_artists")

        merged_df = pd.merge(track_df_exploded, self.artist_df[["id", "genres"]], left_on="id_artists", right_on="id")

        return merged_df[["name", "artists", "popularity", "genres"]]

    def make_predictions_track(self, data):
        predict_tracks_df = self.tracks_df.loc[self.tracks_df["name"].str.contains(data)]
        predict_tracks_df["release_date"] = pd.to_datetime(predict_tracks_df["release_date"])
        predict_tracks_df = predict_tracks_df.sort_values(by=["release_date"], ascending=False)

        # get the index of the first track
        first_track_index = predict_tracks_df.index[0]

        neighbors = self.annoy_loaded.get_nns_by_item(first_track_index, 10)

        result = self.tracks_df.loc[neighbors]

        track_df_exploded = result.explode("id_artists")

        merged_df = pd.merge(track_df_exploded, self.artist_df[["id", "genres"]], left_on="id_artists",
                                 right_on="id")

        return merged_df[["name", "artists", "popularity", "genres"]]