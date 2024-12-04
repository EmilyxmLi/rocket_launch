import math as m
#CONSTANTS
ROCKET_DENSITY= 1.225
#constant of rocket density in kg/m**3
SPACE_FUEL_LOW= 100000.00
#constant maximum mass for low space fuel use 
SPACE_FUEL_MED= 400000.00
#constant maximum mass for medium space fuel use 
MATERIAL_COST= 5.0
#cost of material per square meter
FUEL_COST = 6.1
#cost of fuel per kg
TAX = 0.15
#tax percent in Quebec
def feet_to_meter(feet):
    '''
    returns conversion of feet to meters rounded
    to 2 decimal places 
    Parameters:
        feet = length in feet (positive float)
    Returns:
        meters = length in meters(positive float)
    Examples:
    >>> feet_to_meter(5.0)
    1.52
    >>> feet_to_meter(12.3)
    3.75
    >>> feet_to_meter(0.02)
    0.01    
    '''
    meters = feet/3.28
    #conversion rate from feet to meters 
    return round(meters,2)


def rocket_volume(radius,height_cone,height_cyl):
    '''
    calculates the volume of a rocket (in m**3)
    Parameters:
        radius = length in meters (positive float)
        height_cone = height in meters (positive float)
        height_cyl = height in meters (positive float)
    Returns :
    rocket_volume = volume in m**3 (positive float)
    Examples:
    >>>rocket_volume(3,5,7)
    245.04
    >>>rocket_volume(2.0,7.0, 3.0)
    67.02
    >>>rocket_volume(100.00,0.02,10)
    314368.7
    
    
    '''
    #adds volumes of the cone and cylinder to find volume
    volume_cone = (m.pi * (radius**2) * (height_cone /3))
    volume_cyl = (m.pi* (radius**2) *height_cyl)
    volume_rocket = (volume_cone + volume_cyl)
    return round(volume_rocket,2)

def rocket_area(radius, height_cone, height_cyl):
    '''
    calculates the area of a rocket in (m**2)
    Parameters:
        radius = length in meters (positive float)
        height_cone = height in meters (positive float)
        height_cyl = height in meters (positive float)
    Returns:
    rocket_area = area in m**2 (positive float)
    Examples:
    >>>rocket_area(2.0,7.0,3.0)
    96.01
    >>>rocket_area(1.2,3.9,9.0)
    87.77
    >>>rocket_area(100.0,0.3,12.0)
    70371.82
    '''
    #calculates the surface area of the
    #rocket by adding cone and cylinder 
    area_cone = (m.pi * radius) * \
    (radius+(m.sqrt(height_cone**2 + radius**2)))
    area_cylinder = (2* m.pi *radius )* (height_cyl + radius)
    area_rocket = area_cone + area_cylinder\
    -(2*(m.pi * (radius**2)))
    return round(area_rocket, 2)

def rocket_mass(radius, height_cone, height_cyl):
    '''
    calculates the mass of a rocket in kg
    Parameters:
        radius = length in meters (positive float)
        height_cone = height in meters (positive float)
        height_cyl = height in meters (positive float)
    Returns:
    rocket_mass = mass in kg (positive float)
    Examples:
    >>>rocket_mass(3.0,10.0,12.0)
    531.09
    >>>rocket_mass(12.52,13.22,0.1)
    2718.63
    >>>rocket_mass(50.55,100.02,123.65)
    1543832.82
    '''
    #calculates the mass of the rocket itself 
    mass=((rocket_volume(radius,
    height_cone, height_cyl))*ROCKET_DENSITY)
    return round(mass,2)
    
    
def rocket_fuel(radius, height_cone, \
height_cyl, velocity_e, velocity_i, time):
    '''
    calculates the fuel necessary to run the rocket,
    factors length  of orbit,mass of rocket,
    and initial/exhaust velocity
    Parameters:
        radius = length in meters (positive float)
        height_cone= height in meters (positive float)
        height_cyl = height in meters (positive float)
        velocity_e = exhuast velocity in m/s (positive float)
        velocity_i = exhaust velocity in m/s (positive float)
        time = period of time in seconds (positive float)
    Returns:
    rocket_fuel = fuel used by rocket in kg (positive float)
    Examples:
    >>>rocket_fuel(50.0,100.0,800.0,700.0,300.0,120.0)
    4616444.53
    >>>rocket_fuel(12.3,153.8,167.9,289.8,200.31,500.2)
    1127509.64
    >>>rocket_fuel(0.39,0.123,0.52,0.99,1.98,50.62)
    68845.31
    '''
    #calculates the amount of fuel the rocket needs
    #depending on the mass of the rocket 
    if rocket_mass(radius, height_cone,height_cyl) <= SPACE_FUEL_LOW:
        fuel_space = 1360 * time
        #lower mass threshhold in space
    elif SPACE_FUEL_LOW <rocket_mass(radius,
    height_cone,height_cyl) <= SPACE_FUEL_MED:
        fuel_space = 2000 * time
        #middle mass threshhold in space
    else:
        fuel_space = 2721 * time
        #all higher masses threshhold in space
    fuel_earth=(rocket_mass(radius, height_cone,
    height_cyl)*(m.e**(velocity_i/velocity_e)-1))
    #calculates the fuel needed from earth
    fuel= fuel_earth + fuel_space 
    return(round(fuel,2))


def calculate_cost(radius, height_cone, height_cyl,\
velocity_e, velocity_i, time, tax):
    '''
    calculates the approximate cost of building and launching rocket 
     Parameters:
        radius = length in meters (positive float)
        height_cone= height in meters (positive float)
        height_cyl = height in meters (positive float)
        velocity_e = exhuast velocity in m/s (positive float)
        velocity_i = exhaust velocity in m/s (positive float)
        time = period of time in seconds (positive float)
        tax = boolean
    Returns:
        cost (in $) = cost of rocket (positive float)
    Examples:
    >>>calculate_cost(50.0,100.0,800.0,700.0,300.0,120.0, False)
    29544028.78
    >>>calculate_cost(12.3,13.6,200.3,109.93,1302.0,130.1, True)
    116484792200.5
    >>>calculate_cost(0.12,1.2,10.09,113.0,0.01,9.3, True)
    88772.35
    '''
    #calculates the total cost of the rocket 
    cost_mat= rocket_area(radius,height_cone, height_cyl)* MATERIAL_COST
    # finds the cost of materials 
    cost_fuel= rocket_fuel(radius, height_cone, height_cyl,
    velocity_e, velocity_i, time) * FUEL_COST
     # cost of fuel
    if tax:
        cost_tax = (cost_mat + cost_fuel)* TAX
        cost= cost_mat + cost_fuel + cost_tax
    else:
        cost = cost_mat + cost_fuel
        #total cost of materials 
    return (round(cost,2))

    
def compute_storage_space(rocket_radius, rocket_cyl_h):
    '''
    Computes the dimensions of the rocket's
    rectangular prism storage space
    Parameters:
        rocket_radius: radius of the rocket in meters (positive float)
        rocket_cyl_h: rocket cylinder height in meters (positive float)
    Returns:
        length_rocket= length of rocket storage space (positive float)
        width_rocket= width of rocket storage space (positive float)
        height_rocket = height of rocket storage space (positive float)
    Examples:
    >>> compute_storage_space(3.0,5.0)
    (4.24, 4.24, 2.5)
    >>> compute_storage_space(2.4,10.0)
    (3.39, 3.39, 5.0)
    >>> compute_storage_space(344.02,1012.0)
    (486.52, 486.52, 506.0)
    
    '''
    #finds length of rocket
    length_rocket = m.sqrt(2) * rocket_radius
    #finds width of rocket 
    width_rocket = m.sqrt(2) * rocket_radius
    #finds the height of rocket 
    height_rocket = rocket_cyl_h / 2
    return(round(length_rocket,2),(
    round(width_rocket,2)),(round(height_rocket,2)))
    #calculates the volume of the storage space 
    
def load_rocket(rocket_weight_i, rocket_radius, rocket_cyl_h):
    '''
    Asks user for length, width, and height of items to
    be loaded onto rocket
    calculates the total mass of the all added items
    restricts the weight and volume of items
    Parameters:
        rocket_weight_i: initial weight of rocket in kg (positive float)
        rocket_radius: radius of rocket in m (positive float)
        rocket_cyl_h: rocket cylinder height in m (positive float)
    Returns:
        total weight of the rocket in kg (positive float)
    Examples:
    >>> load_rocket(399,100,100)
    no more items can be added
    >>>load_rocket(503.2,102.4,112.5)
    Please enter the weight of the next item
    (type "Done" when you are done filling the rocket) 30
    Enter item width 5
    Enter item length 5
    Enter item height 6
    Item could not be added... please try again...
    Please enter the weight of the next item
    (type "Done" when you are done filling the rocket) 21
    Enter item width 4
    Enter item length 4
    Enter item height 4
    Please enter the weight of the next item  (type
    "Done" when you are done filling the rocket) Done
    524.2
    >>> load_rocket(20053,133,1940)
    Please enter the weight of the next item  (type
    "Done" when you are done filling the rocket)19
    Enter item width 10
    Enter item length 10
    Enter item height 10
    Item could not be added... please try again...
    Please enter the weight of the next item  (type
    "Done" when you are done filling the rocket)400 
    Enter item width 300 
    Enter item length 500 
    Enter item height 120
    Item could not be added... please try again...
    Please enter the weight of the next item  (type
    "Done" when you are done filling the rocket)300 
    Enter item width20
    Enter item length 20 
    Enter item height 20
    Please enter the weight of the next item  (type
    "Done" when you are done filling the rocket)Done
    20353.0
    '''
    weight = 0
    total_vol = 0 
    max_total_weight = rocket_weight_i * 0.05
    #calculates the maximum weight the rocket can hold 
    if rocket_weight_i < 400:
        print('no more items can be added')
        #rocket cannot hold items if initial weight is less than 400
    else:
        length, width, height = compute_storage_space\
        (rocket_radius,rocket_cyl_h)
        item_weight = (input('Please enter the weight of the next\
item(type \"Done\" when you are done filling the rocket)'))
        max_vol_total = length * width * height* 0.4
        while item_weight != "Done":
            item_width = float(input('Enter item width'))
            item_length = float(input('Enter item length'))
            item_height = float(input('Enter item height'))
            item_w = float(item_weight)
            item_vol = item_width * item_length * item_height
            #takes users inputs of the dimensions of object and calculates it's volume 
            if 20.0 <= item_w <= 500.0 and (item_w + weight) < max_total_weight \
            and item_vol > 0.125 and (total_vol+item_vol) < max_vol_total:
            #sees whether item can or cannot be loaded 
                weight += item_w
                total_vol += item_vol
                item_weight = (input('Please enter the weight of the\
next item \(type \"Done\" when you are done filling the rocket)'))
            elif weight >= (max_total_weight - 20) or total_vol > max_vol_total:
                print('No more items can be added')
                item_weight ="Done"
            else:
                print('Item could not be added... please try again...')        
                item_weight =(input('Please enter the weight\
of the next item  (type \"Done\" when you are done filling the rocket)'))
    total_weight = float(weight + rocket_weight_i)
    #calculates the total weight of rocket after loading 
    return round(total_weight,2)

def projectile_sim(simulation_time, interval, v0, angle):
    '''
    simulates rocket's projectile motion by taking time of simulation,
    interval between data points, angle of launch and initial velocity
    Parameters:
        simulation_time = time in seconds (positive int)
        interval = period between points in seconds (positive int)
        v0 = initial velocity in m/s (positive float)
        angle = angle in radians (positive float
    Returns:
    This function has no returns
    Examples 
    >>> projectile_sim(10,2,100.0,0.79)
    0.0
    122.45
    205.66
    249.63
    254.36
    219.85
    >>> projectile_sim (12,4,12.4,0.2)
    0.0
    >>> projectile_sim(100,2,50,0.9)
    0.0
    58.71
    78.19
    58.42
    '''
    for time in range (0 , simulation_time + 1, interval):
        height =((-1/2) * 9.81 * (time ** 2) + (v0 * m.sin(angle) * time))
        #formula for projectile motion 
        if (round(height,2)) >=0.0:
            print(round(height,2))
        
        
def rocket_main():
    '''
    calculates the total cost of the rocket, total weight
    after loading, and the rocket's flight trajectory
    Parameters:
    none
    Returns:
    none
    Examples:
    >>> rocket_main()
    Welcome to the rocket simulation!
    Enter the rocket radius in feet 12
    Enter the rocket cone height in feet50
    Enter the rocket cylinder height in feet500
    Enter the rocket's exhaust velocity for the upcoming trip500
    Enter the rocket's initial velocity for the upcoming trip200
    Enter the angle of launch of the upcoming trip in rads:0.4
    Enter the length of the upcoming trip (in s):200
    Would you like to factor in tax? 1 for yes, 0 for no:1
    This trip will cost $1957532.38
    Now loading the rocket
    Please enter the weight of the next item  (type "Done"
    when you are done filling the rocket)31
    Enter item width5
    Enter item length5
    Enter item height5
    Please enter the weight of the next item  (type "Done"
    when you are done filling the rocket)12
    Enter item width2
    Enter item length2
    Enter item height2
    Item could not be added... please try again...
    Please enter the weight of the next item  (type "Done"
    when you are done filling the rocket)Done
    8151.53
    Enter the simulation total time: 12
    Enter the simulation interval:1
    Now simulating the rocket trajectory:
    0.0
    72.98
    136.15
    189.51
    233.05
    266.79
    290.72
    304.84
    309.15
    303.65
    288.34
    263.22
    228.28
    >>> rocket_main()
    Welcome to the rocket simulation!
    Enter the rocket radius in feet 15
    Enter the rocket cone height in feet50
    Enter the rocket cylinder height in feet 29
    Enter the rocket's exhaust velocity for the upcoming trip 75
    Enter the rocket's initial velocity for the upcoming trip30
    Enter the angle of launch of the upcoming trip in rads: 0.9
    Enter the length of the upcoming trip (in s): 100
    Would you like to factor in tax? 1 for yes, 0 for no:1
    This trip will cost $961050.33
    Now loading the rocket
    Please enter the weight of the next item  (type
    "Done" when you are done filling the rocket) 20
    Enter item width 3
    Enter item length 3
    Enter item height 3
    Please enter the weight of the next item  (type
    "Done" when you are done filling the rocket)500
    Enter item width500
    Enter item length 500
    Enter item height 500
    Item could not be added... please try again...
    Please enter the weight of the next item  (type
    "Done" when you are done filling the rocket)Done
    1138.82
    Enter the simulation total time: 17
    Enter the simulation interval: 4 
    Now simulating the rocket trajectory:
    0.0
    15.52
    >>> rocket_main()
    Welcome to the rocket simulation!
    Enter the rocket radius in feet 500
    Enter the rocket cone height in feet 125
    Enter the rocket cylinder height in feet 1000
    Enter the rocket's exhaust velocity for the upcoming trip 800
    Enter the rocket's initial velocity for the upcoming trip95
    Enter the angle of launch of the upcoming trip in rads: 0.87
    Enter the length of the upcoming trip (in s):1200
    Would you like to factor in tax? 1 for yes, 0 for no: 1
    This trip will cost $50558363.52
    Now loading the rocket
    Please enter the weight of the next item  (type
    "Done" when you are done filling the rocket)400
    Enter item width 15
    Enter item length 29
    Enter item height 83
    Please enter the weight of the next item  (type
    "Done" when you are done filling the rocket)Done
    28401917.45
    Enter the simulation total time: 16
    Enter the simulation interval: 4
    Now simulating the rocket trajectory:
    0.0
    211.96
    266.97
    165.01
    '''
    print('Welcome to the rocket simulation!')
    radius_f = float(input('Enter the rocket radius in feet'))
    cone_height_f =  float(input('Enter the rocket cone height in feet'))
    cylinder_height_f = float(input('Enter the rocket \
cylinder height in feet'))
    velocity_e = float(input('Enter the rocket\'s \
exhaust velocity for the upcoming trip'))
    velocity_i = float(input('Enter the rocket\'s \
initial velocity for the upcoming trip'))
    angle = float(input('Enter the angle of launch \
of the upcoming trip in rads:'))
    time = float(input('Enter the length of the \
upcoming trip (in s):'))
    tax= (input('Would you like to factor in tax? \
1 for yes, 0 for no:'))
    #takes user inputs of rocket information
    radius = feet_to_meter(radius_f)
    height_cone = feet_to_meter(cone_height_f)
    height_cyl = feet_to_meter(cylinder_height_f)
    #converts feet to meters for dimensions 
    if tax != 0:
        tax = True
    else:
        tax= False
    cost = str(calculate_cost(radius, height_cone, \
    height_cyl, velocity_e, velocity_i, time, tax))
    #calculates cost of rocket 
    print('This trip will cost $' + cost)
    print('Now loading the rocket')
    rocket_weight_i = rocket_mass(radius, height_cone, height_cyl)
    #calculates the initial weight of rocket 
    rocket_loaded = load_rocket(rocket_weight_i,radius, height_cyl)
    print(rocket_loaded)
    sim_time = int(input('Enter the simulation total time:'))
    interval = int(input('Enter the simulation interval:'))
    print('Now simulating the rocket trajectory:')
    projectile_sim(sim_time, interval, velocity_i, angle)
    #simulates the rocket's motion after loading rocket
       

    
    
    
        