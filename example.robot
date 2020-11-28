-> RandomWalk {
	on clap -> ShutDown

	-> MovingForward {
		move forward at speed 10
		on obstacle -> Avoid
	}

	Avoid {
		move backward for 1 s
		turn by random (-180, 180)
	} -> MovingForward
	
	ShutDown { return to base }
}