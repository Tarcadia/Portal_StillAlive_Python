#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# The copyright for song <Still Alive> belongs to Jonathan Coulton and Valve Software
# The copyright for code <still_alive_credit.py> belongs to LHF (BD4SUP)
# Contact me if there's copyright violation and if deletion of the content is needed.
#
#
#
# telnet_cast.py by Tarcadia
# November 2021
#


import socket;
import subprocess;
import os;
import threading;



class shell(threading.Thread):

    def __init__(self, shell, conn) -> None:
        super().__init__();
        self.shell = shell;
        self.conn = conn;
        return;

    def run(self) -> None:
        conn = self.conn;
        pipe = os.popen(self.shell, mode = 'r');
        try:
            while True:
                b = pipe.read(1);
                conn.send(bytes(b, 'ascii'));
                if not b:
                    conn.shutdown(socket.SHUT_RDWR);
                    pipe.close();
                    break;
        except Exception as err:
            print(err);
            conn.close();
            pipe.close();



#host = socket.gethostname();
#port = 6023;
host = '127.0.0.1'
port = 23;
backlog = 16;
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
server.bind((host, port));
server.listen(backlog);

while True:
    try:
        conn, addr = server.accept();
        print(addr);
        user = shell(shell = 'python ./still_alive_credit_fortelnet.py', conn = conn);
        user.start();
    except BlockingIOError:
        pass;

