import os

def select_modulation():
    print("\nYou have selected an Analog Signal\n")
    modulation_option = input(
        "Choose the modulation technique you want to apply:\n"
        "1. Pulse Code Modulation (PCM)\n"
        "2. Delta Modulation (DM)\n"
    )
    
    if int(modulation_option) == 1:
        os.system("python pcm.py")  # Run PCM encoding script
    else:
        os.system("python delta_modulation.py")  # Run DM encoding script

def select_line_encoding():
    print("\nYou have selected a Digital Signal\n")
    encoding_option = int(input(
        "Choose the line encoding technique you wish to implement:\n"
        "1. NRZ-L\n"
        "2. NRZ-I\n"
        "3. Manchester\n"
        "4. Differential Manchester\n"
        "5. AMI\n"
    ))

    if encoding_option == 1:
        os.system("python NRZL.py")  # Run NRZ-L encoding script
    elif encoding_option == 2:
        os.system("python NRZI.py")  # Run NRZ-I encoding script
    elif encoding_option == 3:
        os.system("python manchester.py")  # Run Manchester encoding script
    elif encoding_option == 4:
        os.system("python DIFFERENTIAL_MANCHESTER.py")  # Run Differential Manchester encoding script
    elif encoding_option == 5:
        select_ami_encoding()  # Handle AMI encoding

def select_ami_encoding():
    ami_option = int(input("Choose your AMI option:\n1. With Scrambling\n2. Without Scrambling\n"))
    
    if ami_option == 1:
        scrambling_method = int(input("Choose scrambling technique:\n1. B8ZS\n2. HDB3\n"))
        if scrambling_method == 1:
            os.system("python B8ZS.py")  # Run B8ZS encoding script
        else:
            os.system("python HDB3.py")  # Run HDB3 encoding script
    else:
        os.system("python AMI.py")  # Run basic AMI encoding script

if __name__ == '__main__':
    signal_choice = input("What type of signal are you working with?\n1. Analog Signal\n2. Digital Signal\n")
    
    if int(signal_choice) == 1:
        select_modulation()  # Process Analog signal with modulation techniques
    else:
        select_line_encoding()  # Process Digital signal with line encoding techniques
