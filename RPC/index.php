<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chess</title>
    <link rel="stylesheet" href="css/mystyles.css">
</head>
<body>
    <div id = "fakeContainer">
        <div id = "boardContainer">
            <div id = "outerboard">
                <div id = "innerboard">
                    <div id = "a_Rank">
                        <div class = "square2" id = "a8"></div>
                        <div class = "square" id = "a7"></div>
                        <div class = "square2" id = "a6"></div>
                        <div class = "square" id = "a5"></div>
                        <div class = "square2" id = "a4"></div>
                        <div class = "square" id = "a3"></div>
                        <div class = "square2" id = "a2"></div>
                        <div class = "square" id = "a1"></div>
                    </div>
                    <div id = "b_Rank">
                        <div class = "square" id = "b8"></div>
                        <div class = "square2" id = "b7"></div>
                        <div class = "square" id = "b6"></div>
                        <div class = "square2" id = "b5"></div>
                        <div class = "square" id = "b4"></div>
                        <div class = "square2" id = "b3"></div>
                        <div class = "square" id = "b2"></div>
                        <div class = "square2" id = "b1"></div>
                    </div>
                    <div id = "c_Rank">
                        <div class = "square2" id = "c8"></div>
                        <div class = "square" id = "c7"></div>
                        <div class = "square2" id = "c6"></div>
                        <div class = "square" id = "c5"></div>
                        <div class = "square2" id = "c4"></div>
                        <div class = "square" id = "c3"></div>
                        <div class = "square2" id = "c2"></div>
                        <div class = "square" id = "c1"></div>
                    </div>
                    <div id = "d_Rank">
                        <div class = "square" id = "d8"></div>
                        <div class = "square2" id = "d7"></div>
                        <div class = "square" id = "d6"></div>
                        <div class = "square2" id = "d5"></div>
                        <div class = "square" id = "d4"></div>
                        <div class = "square2" id = "d3"></div>
                        <div class = "square" id = "d2"></div>
                        <div class = "square2" id = "d1"></div>
                    </div>
                    <div id = "e_Rank">
                        <div class = "square2" id = "e8"></div>
                        <div class = "square" id = "e7"></div>
                        <div class = "square2" id = "e6"></div>
                        <div class = "square" id = "e5"></div>
                        <div class = "square2" id = "e4"></div>
                        <div class = "square" id = "e3"></div>
                        <div class = "square2" id = "e2"></div>
                        <div class = "square" id = "e1"></div>
                    </div>
                    <div id = "f_Rank">
                        <div class = "square" id = "f8"></div>
                        <div class = "square2" id = "f7"></div>
                        <div class = "square" id = "f6"></div>
                        <div class = "square2" id = "f5"></div>
                        <div class = "square" id = "f4"></div>
                        <div class = "square2" id = "f3"></div>
                        <div class = "square" id = "f2"></div>
                        <div class = "square2" id = "f1"></div>
                    </div>
                    <div id = "g_Rank"> 
                        <div class = "square2" id = "g8"></div>
                        <div class = "square" id = "g7"></div>
                        <div class = "square2" id = "g6"></div>
                        <div class = "square" id = "g5"></div>
                        <div class = "square2" id = "g4"></div>
                        <div class = "square" id = "g3"></div>
                        <div class = "square2" id = "g2"></div>
                        <div class = "square" id = "g1"></div>
                    </div>
                    <div id = "h_Rank">
                        <div class = "square" id = "h8"></div>
                        <div class = "square2" id = "h7"></div>
                        <div class = "square" id = "h6"></div>
                        <div class = "square2" id = "h5"></div>
                        <div class = "square" id = "h4"></div>
                        <div class = "square2" id = "h3"></div>
                        <div class = "square" id = "h2"></div>
                        <div class = "square2" id = "h1"></div>
                    </div>
                </div>
            </div>
        </div>
        <div id = "upgradesContainer">
            <div id = "upgrade1" class = "upgrade">
                <p id = "title">Upgrade 1</p>
            </div>
            <div id = "upgrade2" class = "upgrade">
                <p id = "title">Upgrade 2</p>
            </div>
            <div id = "upgrade3" class = "upgrade">
                <p id = "title">Upgrade 3</p>
            </div>
        </div>
        <div id = "currentUpgradesContainer">
        
        </div>
    </div>
    <script src="scripts/RPC.js"></script>
</body>
</html>