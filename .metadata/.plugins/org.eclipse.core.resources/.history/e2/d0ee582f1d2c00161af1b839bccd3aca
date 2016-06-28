################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../sources/hal/uart/debugUart.c \
../sources/hal/uart/fsl_debug_console.c \
../sources/hal/uart/interpreter.c \
../sources/hal/uart/print_scan.c 

OBJS += \
./sources/hal/uart/debugUart.o \
./sources/hal/uart/fsl_debug_console.o \
./sources/hal/uart/interpreter.o \
./sources/hal/uart/print_scan.o 

C_DEPS += \
./sources/hal/uart/debugUart.d \
./sources/hal/uart/fsl_debug_console.d \
./sources/hal/uart/interpreter.d \
./sources/hal/uart/print_scan.d 


# Each subdirectory must supply rules for building sources it contributes
sources/hal/uart/%.o: ../sources/hal/uart/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross ARM C Compiler'
	arm-none-eabi-gcc -mcpu=cortex-m0plus -mthumb -O0 -fmessage-length=0 -fsigned-char -ffunction-sections -fdata-sections  -g3 -D"CPU_MKL25Z128VLK4" -I"../Sources" -I"../Project_Settings/Startup_Code" -I"../SDK/platform/CMSIS/Include" -I"../SDK/platform/devices" -I"../SDK/platform/devices/MKL25Z4/include" -I"C:\Freescale\KSDK_1.2.0/platform/utilities/inc" -I"C:\Freescale\KSDK_1.2.0/platform/utilities/src" -I"C:\Freescale\KSDK_1.2.0\platform\hal\inc" -I"C:\Freescale\KSDK_1.2.0\platform\system\inc" -I"C:\Freescale\KSDK_1.2.0\platform\osa\inc" -I"C:\Freescale\KSDK_1.2.0\platform\drivers\inc" -std=c99 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -c -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


