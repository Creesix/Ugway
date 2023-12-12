/*
* Phidget Hello World Program for all devices
* (c) Phidgets 2017
*/


#include <stdio.h>
#include <stdlib.h>
#include <phidget22.h>

void LocalErrorCatcher(int errorCode);

// -------------------- Event Functions ---------------------------------------

void CCONV AttachHandler(PhidgetManagerHandle manager, void *userptr, PhidgetHandle device) {

	int serialNumber;
	const char *name;

	LocalErrorCatcher(
		Phidget_getDeviceName(device, &name));
	LocalErrorCatcher(
		Phidget_getDeviceSerialNumber(device, &serialNumber));

	printf("Hello Device %s, Serial Number: %d\n", name, serialNumber);

	return;
}

void CCONV DetachHandler(PhidgetManagerHandle manager, void *userptr, PhidgetHandle device) {

	int serialNumber;
	const char *name;

	LocalErrorCatcher(
		Phidget_getDeviceName(device, &name));
	LocalErrorCatcher(
		Phidget_getDeviceSerialNumber(device, &serialNumber));

	printf("Goodbye Device %s, Serial Number: %d\n", name, serialNumber);

	return;
}

// This error handler can handle any Phidget function that returns an int
void LocalErrorCatcher(int errorCode) {

	const char *errorDescription;
	PhidgetReturnCode ret;

	// If the error code is 0, everything is okay
	if (errorCode != EPHIDGET_OK) {

		// Otherwise, you can print specific messages or perform actions by error value.
		// Here we will simply print the error and exit
		switch (errorCode) {
		default:
			printf("Error: An error occurred with return code %d.\n", errorCode);

			ret = Phidget_getErrorDescription(errorCode, &errorDescription);
			if (ret != EPHIDGET_OK) {
				printf("Phidget_getErrorDescription failed. Exiting...\n");
				exit(1);
			}

			printf("Error Description: %s\n", errorDescription);
			printf("Exiting...\n");
			exit(1);
		}
	}
	return;
}

// -------------------- Main Code ---------------------------------------------

int main(int argc, char* argv[]) {

	PhidgetManagerHandle manager = 0;
	LocalErrorCatcher(
		PhidgetManager_create(&manager));

	LocalErrorCatcher(
		PhidgetManager_setOnAttachHandler(manager,
			AttachHandler, NULL));

	LocalErrorCatcher(
		PhidgetManager_setOnDetachHandler(manager,
			DetachHandler, NULL));

	printf("Opening...\n");

	// Most opening and closing would be via a cast to
	// (PhidgetHandle), however, this manager has its
	// own handle struct to cast to.
	LocalErrorCatcher(
		PhidgetManager_open(manager));

	printf("Phidget Simple Playground (plug and unplug managers)\n");
	printf("Press Enter to end anytime...\n");
	getchar();

	printf("Closing...\n");
	LocalErrorCatcher(
		PhidgetManager_close(manager));
	LocalErrorCatcher(
		PhidgetManager_delete(&manager));

	return 0;
}
