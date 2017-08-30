#
# Copyright (c) 2017, Stephanie Wehner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. All advertising materials mentioning features or use of this software
#    must display the following acknowledgement:
#    This product includes software developed by Stephanie Wehner, QuTech.
# 4. Neither the name of the QuTech organization nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from SimulaQron.general.hostConfig import *
from SimulaQron.cqc.backend.cqcHeader import *
from SimulaQron.cqc.pythonLib.cqc import *

def prep(cqc):
	q=qubit(cqc,print_info=False)
	q.H(print_info=False)
	return q

#####################################################################################################
#
# main
#
def main():

	# In this example, we are Alice.
	myName="Alice"

	# Initialize the connection
	cqc=CQCConnection(myName)

	# # Do tomography
	# freqs=cqc.tomography(prep,100)
	# print("f_X: {}".format(freqs[0]))
	# print("f_Y: {}".format(freqs[1]))
	# print("f_Z: {}".format(freqs[2]))

	# Test
	ans=cqc.test_preparation(prep,(0,0.5,0.5),None,iterations=1000)
	print(ans)


	# Stop the connection
	cqc.close()



##################################################################################################
main()

