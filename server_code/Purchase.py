import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def charge_user(email, asset_id):
    asset = app_tables.assets.get(id=asset_id)
    
    if asset is None:
        raise Exception("Asset not found")  # Handle this case as needed
    
    total = asset['total']
    user = anvil.users.get_user()
    
    if user["purchased_assets"] is None:
        user["purchased_assets"] = []
    
    if asset_id in user["purchased_assets"]:
        return  # Asset already purchased, no need to charge again
    user["purchased_assets"] = user["purchased_assets"] + [asset_id]

