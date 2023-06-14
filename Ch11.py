#!/usr/bin/env python3
import os
import psutil

# Script Name:                  Psutil
# Author:                       NATASHA SIRAMARCO
# Date of latest revision:      06/14/2023
# Purpose:                      Install Psutil.
#                               Create a Python script that fetches this information using Psutil:
#                                   Time spent by normal processes executing in user mode
#                                   Time spent by processes executing in kernel mode
#                                   Time when system was idle
#                                   Time spent by priority processes executing in user mode
#                                   Time spent waiting for I/O to complete.
#                                   Time spent for servicing hardware interrupts
#                                   Time spent for servicing software interrupts
#                                   Time spent by other operating systems running in a virtualized environment
#                                   Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
                           
# Declaration of variables

# Declaration of functions

# Main
# User mode
user_mode = psutil.cpu_times().user
print("User Mode:", user_mode)

# Kernel mode
kernel_mode = psutil.cpu_times().system
print("Kernel Mode:", kernel_mode)

# System idle
system_idle = psutil.cpu_times().idle
print("System Idle:", system_idle)

# Priority in user mode
priority_user_mode = psutil.cpu_times().nice
print("Priority User Mode:", priority_user_mode)

# I/O to completion
io_completion = psutil.cpu_times().iowait
print("I/O Completion Time:", io_completion)

#Servicing hardware interrupts
irq_inturrupts = psutil.cpu_times().irq
print("Hardware Interrupts:", irq_inturrupts)

# Servicing software interrupts
software_irq_time = psutil.cpu_times().softirq
print("Software Interrupts:", software_irq_time)

# OS running in virtualized environment
steal_time = psutil.cpu_times().steal
print("Virtualized OS:", steal_time)

# Virtual CPU for guest OS
guest_time = psutil.cpu_times().guest
print("Guest OS:", guest_time)

# Virtual CPU for guest OS under Linux kernel
guest_nice_linux = psutil.cpu_times().guest_nice
print("Guest OS under Linux:", guest_nice_linux)

# End