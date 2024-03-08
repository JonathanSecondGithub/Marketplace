def hamdle_response(message):
    p_message = message.lower()

    if p_message == '!help':
        return "`Help message!`"
    
    if p_message == '1':
        return "`TechTech Solutions` \n`FreshHarvest Farms` \n`FashionFusion Apparel` \n`HealthWell Pharmaceuticals` "
    
    if p_message == 'techtech solutions':
        return "`Computers (Desktops, Laptops, Workstations)` `Smartphones and Tablets` `Computer Accessories (Keyboards, Mice, Monitors, Cables)` `Networking Equipment (Routers, Switches, Access Points)` "