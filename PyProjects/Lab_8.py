"""
1. (25) 17-20 (identifiers)

2. (25) 18-1 (processes vs. threads)

3. (25) 18-2 (threads & Python)

4. (25) 19-1 (client-server architecture)

"""
#----------------------------------------------------------------------
#17-20
"""
It may overshadow any built-in methods/functions with that name. Thus it is used with an underscore.

"""
#----------------------------------------------------------------------
#18-1
"""
Process:
A process is a discrete execution of a program. Has its own memory, data stack,
and thus fairly independent of each other; they are also ran separately, and cannot communicate natively with each other.

Threads:
A thread is a indiscrete execution of a program and does NOT have its own data stack,
memory, etc. Threads share the same data space and thus can share information natively.  
They can can be executed in parallel, for all intents and purposes. 
"""
#----------------------------------------------------------------------
#18-2
"""
I/O bound. Since CPU bound will create overhead to simulate parallelism, thus making it slower
"""
#----------------------------------------------------------------------
#19-1
"""
Windows Server will send data (such as bytes, inputs, colors) to a receiving Windows Client (to display or process). The amount depends on what the Windowing Client asks

Of course the roles can be reversed (Server receives, client sends), but generally speaking server sends and clients receives
"""