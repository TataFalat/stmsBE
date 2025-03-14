Simple Transport Management System Demo

/stmsBE contains Django REST api backend sqlite server
/stmsFE contains Vue frontend

Order has waypoints[] containing all attached waypoints
Waypoint type uses enum, postalCode, city and country are strings, but in real life scenarios codelists/dictionaries would be preferrable

Order has to have at least 1 waypoint, but it is checked in the frontend only, check can be added to BE view, if needed
Order list can be filtered
Order can be removed, displays/hides attached waypoints, if clicked on the row
Orders and OrderList components could by further decomposed, e.g Order to OrderForm and WaypointsForm, OrderList to OrderFilter
Api calls could be moved to standalone apiService file
