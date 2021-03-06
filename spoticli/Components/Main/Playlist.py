from spoticli.Components.Templates.Menu import Menu
from spoticli.Components.Main.SongItem import SongItem
from spoticli.Utils.api import spotifyGetAPI

class Playlist(Menu):

    def __init__(self, name, playlistId):
        response = spotifyGetAPI(f"/playlists/{playlistId}/tracks", cache=True, paged=True)
        items = []
        for track in response:
            items.append(SongItem(track, f"spotify:playlist:{playlistId}"))
        super().__init__(name, items)
        self.playlistId = playlistId
