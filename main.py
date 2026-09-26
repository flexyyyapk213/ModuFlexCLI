# ModuFlexUI
# Copyright (C) 2026 flexyyyapk213

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import flet as ft

class ModuFlexGUI:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.title = "ModuFlexGUI"
        self.page.theme_mode = ft.ThemeMode.DARK

        self.page.on_view_pop = self.view_pop
        self.page.on_route_change = self.route_change

        self.busy_views = {}
        self.rooms = {
            "/": self.main_room
        }

        self.page.route = '/'
        self.page.views.append(self.main_room())
        self.page.update()
    
    def view_pop(self, e):
        self.page.views.pop()
        
        top_view = self.page.views[-1]
        self.page.route = top_view.route
    
    def main_room(self) -> ft.View:
        return ft.View(route='/', controls=[ft.Text(value='Hello from ModuFlexGUI')])
    
    def route_change(self, e: ft.RouteChangeEvent):
        self.page.views.clear()
        
        route = e.route
        if self.busy_views.get(route) is None and self.rooms.get(route) is not None:
            self.busy_views[route] = self.rooms[route]
        else:
            self.page.views.append(self.unknown_route(e))
            self.page.update()
            return
        
        self.page.views.append(self.busy_views[route]())
        self.page.update()
    
    def unknown_route(self, e: ft.RouteChangeEvent):
        return ft.View(route=e.route, controls=[ft.Text(value='Unknown route. Please, go to the main page.')])

if __name__ == "__main__":
    ft.run(ModuFlexGUI, view=ft.AppView.WEB_BROWSER)
