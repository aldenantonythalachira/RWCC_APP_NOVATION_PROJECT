import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def get_asset_details(asset_id):
    return app_tables.assets.get(id=asset_id)

@anvil.server.callable
def get_all_assets():
    return app_tables.assets.client_readable()
