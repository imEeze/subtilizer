if not LPH_OBFUSCATED then --  set these if not obfuscated so your script can run without obfuscation for when you are testing
    LPH_JIT_ULTRA = function(...)
        return (...)
    end
    LPH_JIT_MAX = function(...)
        return (...)
    end
end
-- dne exclusive
local Library = loadstring(game:HttpGet("https://raw.githubusercontent.com/bloodball/-back-ups-for-libs/main/cat"))()
local LinoriaNotifs = loadstring(game:HttpGet("https://pastebin.com/raw/T8K6dsf3"))()
getgenv().WatermarkColor = Color3.fromRGB(255, 0, 125)
local DLib = loadstring(game:HttpGet("https://raw.githubusercontent.com/dnelol/3d-drawing/main/code.lua"))()
local StrafeVisualss = DLib:New3DCircle()

local AnimationModule = {
    Astronaut = {
        "rbxassetid://891621366",
        "rbxassetid://891633237",
        "rbxassetid://891667138",
        "rbxassetid://891636393",
        "rbxassetid://891627522",
        "rbxassetid://891609353",
        "rbxassetid://891617961"
    },
    Bubbly = {
        "rbxassetid://910004836",
        "rbxassetid://910009958",
        "rbxassetid://910034870",
        "rbxassetid://910025107",
        "rbxassetid://910016857",
        "rbxassetid://910001910",
        "rbxassetid://910030921",
        "rbxassetid://910028158"
    },
    Cartoony = {
        "rbxassetid://742637544",
        "rbxassetid://742638445",
        "rbxassetid://742640026",
        "rbxassetid://742638842",
        "rbxassetid://742637942",
        "rbxassetid://742636889",
        "rbxassetid://742637151"
    },
    Confindent = {
        "rbxassetid://1069977950",
        "rbxassetid://1069987858",
        "rbxassetid://1070017263",
        "rbxassetid://1070001516",
        "rbxassetid://1069984524",
        "rbxassetid://1069946257",
        "rbxassetid://1069973677"
    },
    Cowboy = {
        "rbxassetid://1014390418",
        "rbxassetid://1014398616",
        "rbxassetid://1014421541",
        "rbxassetid://1014401683",
        "rbxassetid://1014394726",
        "rbxassetid://1014380606",
        "rbxassetid://1014384571"
    },
    Default = {
        "http://www.roblox.com/asset/?id=507766666",
        "http://www.roblox.com/asset/?id=507766951",
        "http://www.roblox.com/asset/?id=507777826",
        "http://www.roblox.com/asset/?id=507767714",
        "http://www.roblox.com/asset/?id=507765000",
        "http://www.roblox.com/asset/?id=507765644",
        "http://www.roblox.com/asset/?id=507767968"
    },
    Elder = {
        "rbxassetid://845397899",
        "rbxassetid://845400520",
        "rbxassetid://845403856",
        "rbxassetid://845386501",
        "rbxassetid://845398858",
        "rbxassetid://845392038",
        "rbxassetid://845396048"
    },
    Ghost = {
        "rbxassetid://616006778",
        "rbxassetid://616008087",
        "rbxassetid://616013216",
        "rbxassetid://616013216",
        "rbxassetid://616008936",
        "rbxassetid://616005863",
        "rbxassetid://616012453",
        "rbxassetid://616011509"
    },
    Knight = {
        "rbxassetid://657595757",
        "rbxassetid://657568135",
        "rbxassetid://657552124",
        "rbxassetid://657564596",
        "rbxassetid://658409194",
        "rbxassetid://658360781",
        "rbxassetid://657600338"
    },
    Levitation = {
        "rbxassetid://616006778",
        "rbxassetid://616008087",
        "rbxassetid://616013216",
        "rbxassetid://616010382",
        "rbxassetid://616008936",
        "rbxassetid://616003713",
        "rbxassetid://616005863"
    },
    Mage = {
        "rbxassetid://707742142",
        "rbxassetid://707855907",
        "rbxassetid://707897309",
        "rbxassetid://707861613",
        "rbxassetid://707853694",
        "rbxassetid://707826056",
        "rbxassetid://707829716"
    },
    Ninja = {
        "rbxassetid://656117400",
        "rbxassetid://656118341",
        "rbxassetid://656121766",
        "rbxassetid://656118852",
        "rbxassetid://656117878",
        "rbxassetid://656114359",
        "rbxassetid://656115606"
    },
    OldSchool = {
        "rbxassetid://5319828216",
        "rbxassetid://5319831086",
        "rbxassetid://5319847204",
        "rbxassetid://5319844329",
        "rbxassetid://5319841935",
        "rbxassetid://5319839762",
        "rbxassetid://5319852613",
        "rbxassetid://5319850266"
    },
    Patrol = {
        "rbxassetid://1149612882",
        "rbxassetid://1150842221",
        "rbxassetid://1151231493",
        "rbxassetid://1150967949",
        "rbxassetid://1148811837",
        "rbxassetid://1148811837",
        "rbxassetid://1148863382"
    },
    Pirtate = {
        "rbxassetid://750781874",
        "rbxassetid://750782770",
        "rbxassetid://750785693",
        "rbxassetid://750783738",
        "rbxassetid://750782230",
        "rbxassetid://750779899",
        "rbxassetid://750780242"
    },
    Popstar = {
        "rbxassetid://1212900985",
        "rbxassetid://1150842221",
        "rbxassetid://1212980338",
        "rbxassetid://1212980348",
        "rbxassetid://1212954642",
        "rbxassetid://1213044953",
        "rbxassetid://1212900995"
    },
    Princess = {
        "rbxassetid://941003647",
        "rbxassetid://941013098",
        "rbxassetid://941028902",
        "rbxassetid://941015281",
        "rbxassetid://941008832",
        "rbxassetid://940996062",
        "rbxassetid://941000007"
    },
    Robot = {
        "rbxassetid://616088211",
        "rbxassetid://616089559",
        "rbxassetid://616095330",
        "rbxassetid://616091570",
        "rbxassetid://616090535",
        "rbxassetid://616086039",
        "rbxassetid://616087089"
    },
    Rthro = {
        "rbxassetid://2510196951",
        "rbxassetid://2510197257",
        "rbxassetid://2510202577",
        "rbxassetid://2510198475",
        "rbxassetid://2510197830",
        "rbxassetid://2510195892",
        "rbxassetid://02510201162",
        "rbxassetid://2510199791",
        "rbxassetid://2510192778"
    },
    Sneaky = {
        "rbxassetid://1132473842",
        "rbxassetid://1132477671",
        "rbxassetid://1132510133",
        "rbxassetid://1132494274",
        "rbxassetid://1132489853",
        "rbxassetid://1132461372",
        "rbxassetid://1132469004"
    },
    Stylish = {
        "rbxassetid://616136790",
        "rbxassetid://616138447",
        "rbxassetid://616146177",
        "rbxassetid://616140816",
        "rbxassetid://616139451",
        "rbxassetid://616133594",
        "rbxassetid://616134815"
    },
    Superhero = {
        "rbxassetid://782841498",
        "rbxassetid://782845736",
        "rbxassetid://782843345",
        "rbxassetid://782842708",
        "rbxassetid://782847020",
        "rbxassetid://782843869",
        "rbxassetid://782846423"
    },
    Toy = {
        "rbxassetid://782841498",
        "rbxassetid://782845736",
        "rbxassetid://782843345",
        "rbxassetid://782842708",
        "rbxassetid://782847020",
        "rbxassetid://782843869",
        "rbxassetid://782846423"
    },
    Vampire = {
        "rbxassetid://1083445855",
        "rbxassetid://1083450166",
        "rbxassetid://1083473930",
        "rbxassetid://1083462077",
        "rbxassetid://1083455352",
        "rbxassetid://1083439238",
        "rbxassetid://1083443587"
    },
    Werewolf = {
        "rbxassetid://1083195517",
        "rbxassetid://1083214717",
        "rbxassetid://1083178339",
        "rbxassetid://1083216690",
        "rbxassetid://1083218792",
        "rbxassetid://1083182000",
        "rbxassetid://1083189019"
    },
    Zombie = {
        "rbxassetid://616158929",
        "rbxassetid://616160636",
        "rbxassetid://616168032",
        "rbxassetid://616163682",
        "rbxassetid://616161997",
        "rbxassetid://616156119",
        "rbxassetid://616157476"
    }
}

StrafeVisualss.Visible = false
StrafeVisualss.ZIndex = 1
StrafeVisualss.Transparency = 1
StrafeVisualss.Color = Color3.fromRGB(255, 255, 255)
StrafeVisualss.Thickness = 1

--// Lua guard has variables Ill change the 100th and user when released

local BodyParts = {
    "Head",
    "HumanoidRootPart",
    "Torso",
    "UpperTorso",
    "LowerTorso",
    "RightHand",
    "LeftLowerArm",
    "RightLowerArm",
    "RightUpperArm",
    "LeftLowerLeg",
    "LeftUpperLeg",
    "LeftFoot",
    "RightFoot",
    "RightUpperLeg",
    "RightLowerLeg"
}

Library.theme.topheight = 50
Library.theme.accentcolor = Color3.fromRGB(203, 9, 61)
Library.theme.accentcolor2 = Color3.fromRGB(203, 9, 61)
Library.theme.fontsize = 15
Library.theme.titlesize = 17

local CursorPath = Instance.new("ScreenGui")
local Swastika = Instance.new("TextLabel")

CursorPath.Name = "CursorPath"
CursorPath.Parent = game.CoreGui
CursorPath.ZIndexBehavior = Enum.ZIndexBehavior.Sibling

Swastika.Name = "Swastika"
Swastika.Parent = CursorPath
Swastika.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
Swastika.BackgroundTransparency = 1.000
Swastika.BorderSizePixel = 2
Swastika.Position = UDim2.new(0, 0, 0, 0)
Swastika.Size = UDim2.new(0, 93, 0, 84)
Swastika.Font = Enum.Font.SourceSans
Swastika.Text = "卍"
Swastika.TextColor3 = Color3.fromRGB(0, 0, 0)
Swastika.TextSize = 46.000
Swastika.TextTransparency = 0
Swastika.Rotation = 45
Swastika.Visible = false

--[[
local Animations = game.ReplicatedStorage.ClientAnimations

local LeanAnimation = Instance.new("Animation", Animations)
LeanAnimation.Name = "Lean"
LeanAnimation.AnimationId = "rbxassetid://3152375249"

local LayAnimation = Instance.new("Animation", Animations)
LayAnimation.Name = "Lay"
LayAnimation.AnimationId = "rbxassetid://3152378852"

local Dance1Animation = Instance.new("Animation", Animations)
Dance1Animation.Name = "Dance1"
Dance1Animation.AnimationId = "rbxassetid://3189773368"

local Dance2Animation = Instance.new("Animation", Animations)
Dance2Animation.Name = "Dance2"
Dance2Animation.AnimationId = "rbxassetid://3189776546"

local GreetAnimation = Instance.new("Animation", Animations)
GreetAnimation.Name = "Greet"
GreetAnimation.AnimationId = "rbxassetid://3189777795"

local ChestPumpAnimation = Instance.new("Animation", Animations)
ChestPumpAnimation.Name = "Chest Pump"
ChestPumpAnimation.AnimationId = "rbxassetid://3189779152"

local PrayingAnimation = Instance.new("Animation", Animations)
PrayingAnimation.Name = "Praying"
PrayingAnimation.AnimationId = "rbxassetid://3487719500"
]]
local LocalPlayer = game.Players.LocalPlayer
local CC = game.Workspace.CurrentCamera
local LocalMouse = LocalPlayer:GetMouse()

--// Main Table

local Script = {
    Main = {
        Speed = false,
        SpeedPower = 2.5,
        SpeedType = "CFrame",
        InfiniteJump = false,
        FakeMacro = false
    },
    SilentAim = {
        Resolver = false,
        Part = "Head",
        Enabled = false,
        RandomBodyPart = false,
        Prediction = 0.1413
    },
    WorldViusals = {
        Ambient = nil,
        Ambient2 = nil
    },
    AntiAims = {
        JitterBot = false,
        SpinBot = false,
        SpinBotSpeed = 7
    },
    Desync = {
        Velocity = {
            Desync = false,
            Unhittable = false,
            Visualize = false,
            VisualizeColor = Color3.fromRGB(255, 0, 125),
            X = 0,
            Y = 0,
            Z = 0,
            DesyncSpinPower = 0.001,
            DesyncPower = 16
        },
        CFrame = {
            Desync = false,
            RandomMode = false,
            RandomRange = 15,
            AngleX = 0,
            AngleY = 0,
            AngleZ = 0,
            X = 0,
            Y = 0,
            Z = 0
        }
    },
    ShitTalk = {
        Enabled = false,
        Delay = 2,
        Type = "Main"
        --[[
        Emoji
        Chinese
        Main
        ]]
    },
    TargetAim = {
        Enabled = false,
        AirShotFunction = true,
        Notifications = false,
        HitNotifs = false,
        AutoPrediction = false,
        Prediction = 0.1413,
        Part = "HumanoidRootPart",
        SelectedPart = "HumanoidRootPart",
        Resolver = false,
        KnockCheck = false,
        BackWardsBang = false,
        ViewTarget = false,
        LookAt = false,
        RandomBodyPart = false
    },
    CamLock = {
        Enabled = false,
        Prediction = 0.1413,
        AutoPrediction = false,
        Resolver = false,
        Smoothness = 0,
        Part = "Head"
    },
    PartSettings = {
        PartVisible = false,
        PartRainbow = false,
        PartColor = Color3.fromRGB(255, 255, 255),
        PartSize = Vector3.new(10, 10, 10),
        PartTransparency = 0,
        PartMaterial = Enum.Material.Neon,
        PartType = Enum.PartType.Ball
    },
    Tracer = {
        Enabled = true,
        Thickness = 1,
        Color = Color3.fromRGB(255, 255, 255),
        Origin = "Mouse"
    },
    Cursor = {
        Spinning = false,
        Rainbow = false,
        SpinSpeed = 1
    },
    Strafe = {
        Enabled = false,
        DesyncStrafe = false,
        Distance = 10,
        Speed = 5,
        Height = 0,
        Visual = false,
        VisualColor = Color3.fromRGB(255, 0, 0)
    },
    RageBot = {
        Enabled = false,
        Distance = 50,
        LookAt = false,
        Resolver = false
    },
    Ratio = {
        Enabled = false,
        Amount = 80
    },
    Misc = {
        AntiBag = false,
        AutoReload = false,
        Reach = false,
        PickUpMoney = false,
        AntiStomp = false,
        NJCD = false,
        CustomGunSFX = false,
        ID = "rbxassetid://1053296915",
        Volume = 10
    },
    Settings = {
        Watermark = true,
        fpscap = 144,
        Type = "Main",
        CheatName = "osiris"
        --game:GetService("CoreGui").osiris.main.top.title
    }
}

--[[
    },
    Tracer = {
        Enabled = true,
        Thickness = 1 ,
        Color = Color3.fromRGB(255,255,255),
    },
]]
local TargetPart = Instance.new("Part")
TargetPart.Color = Color3.fromRGB(255, 255, 255)
TargetPart.CanCollide = false
TargetPart.Size = Vector3.new(10, 10, 10)
TargetPart.Transparency = 0.8
TargetPart.Material = Enum.Material.Neon
TargetPart.Shape = Enum.PartType.Ball
TargetPart.Parent = game.Workspace
TargetPart.Anchored = true

local FOV = Drawing.new("Circle")
FOV.Filled = false
FOV.Color = Color3.fromRGB(255, 255, 255)
FOV.Visible = false
FOV.Radius = 100000

local Tracer = Drawing.new("Line")
Tracer.Visible = false
Tracer.Thickness = 1
Tracer.Color = Color3.fromRGB(255, 0, 0)

local RandomShitTalk = {
    [1] = {
        "but doctor prognosis: OWNED but doctor prognosis: OWNED but doctor prognosis: OWNED but doctor prognosis: OWNED but doctor prognosis: OWNED but doctor prognosis: OWNED ",
        "but doctor results: 🔥 but doctor results: 🔥 but doctor results: 🔥 but doctor results: 🔥 but doctor results: 🔥 but doctor results: 🔥 but doctor results: 🔥 ",
        "looks like you need to talk to your doctor looks like you need to talk to your doctor looks like you need to talk to your doctor looks like you need to talk to your doctor ",
        "speak to your doctor about this one speak to your doctor about this one speak to your doctor about this one speak to your doctor about this one speak to your doctor about this one ",
        "but analysis: PWNED but analysis: PWNED but analysis: PWNED but analysis: PWNED but analysis: PWNED but analysis: PWNED but analysis: PWNED but analysis: PWNED but analysis: PWNED ",
        "but diagnosis: OWND but diagnosis: OWND but diagnosis: OWND but diagnosis: OWND but diagnosis: OWND but diagnosis: OWND but diagnosis: OWND but diagnosis: OWND but diagnosis: OWND "
    },
    ["Chinese"] = {
        "音频少年公民记忆欲求无尽 heywe 僵尸强迫身体哑集中排水",
        "持有毁灭性的神经重景气游行脸红青铜色类别创意案",
        "诶比西迪伊艾弗吉艾尺艾杰开艾勒艾马艾娜哦屁吉吾",
        "完成与草屋两个苏巴完成与草屋两个苏巴完成与草屋",
        "庆崇你好我讨厌你愚蠢的母愚蠢的母庆崇",
        "坐下，一直保持着安静的状态。 谁把他拥有的东西给了他，所以他不那么爱欠债务，却拒  参加锻炼，这让他爱得更少了",
        ", yīzhí bǎochízhe ānjìng de zhuàngtài. Shéi bǎ tā yǒngyǒu de dōngxī gěile tā, suǒyǐ tā bù nàme ài qiàn zhàiwù, què jùjué cānjiā duànliàn, z",
        "他，所以他不那r给了他东西给了他爱欠s，却拒绝参加锻炼，这让他爱得更UGT少了",
        "有的东西给了他，所以他不那rblx trader captain么有的东西给了他爱欠绝参加锻squidward炼，务，却拒绝参加锻炼，这让他爱得更UGT少了",
        "wocky slush他爱欠债了他他squilliam拥有的东西给爱欠绝参加锻squidward炼",
        "坐下，一直保持着安静的状态 谁把他拥有的东西给了他，所以他不那rblx trader captain么有的东西给了他爱欠债了他他squilliam拥有的东西给爱欠绝参加锻squidward炼，务，却拒绝参加锻炼，这让他爱得更UGT少了",
        "免费手榴弹 hack绕过作弊工作DA HOOD roblox aimbot瞄准无声目标绕过2020工作真正免费下载和使用",
        "zal發明了roblox汽車貿易商的船長ro blocks，並將其洩漏到整個宇宙，還修補了虛假的角神模式和虛假的身體，還發明了基於速度的AUTOWALL和無限制的自動壁紙遊戲 ",
        "彼が誤って禁止されたためにファントムからautowallgamingを禁止解除する請願とそれはでたらめですそれはまったく意味がありませんなぜあなたは合法的なプレーヤーを禁止するのですか ",
        "ジェイソンは私が神に誓う女性的な男の子ではありません ",
        "傑森不是我向上帝發誓女性男孩 "
    },
    ["Emoji"] = {
        "🔥🔥🔥🔥🔥🔥🔥🔥",
        "😅😅😅😅😅😅😅😅",
        "😂😂😂😂😂😂😂😂",
        "😹😹😹😹😹😹😹😹",
        "😛😛😛😛😛😛😛😛",
        "🤩🤩🤩🤩🤩🤩🤩🤩",
        "🌈🌈🌈🌈🌈🌈🌈🌈",
        "😎😎😎😎😎😎😎😎",
        "🤠🤠🤠🤠🤠🤠🤠🤠",
        "😔😔😔😔😔😔😔😔"
    },
    ["Main"] = {
        "brb taking a nap 💤💤💤 ",
        "gonna go take a walk 🚶‍♂️🚶‍♀️🚶‍♂️🚶‍♀️ ",
        "#osiris better XD .gg/dhmscript",
        "osiris user VV 😳😳😳",
        "just a skill issue that you dont have osiris",
        "mad cause no osiris LOL .gg/dhmscript"
    }
}

function CheckWall(head)
    if v == LocalPlayer then
        return false
    end

    local castPoints = {LocalPlayer.Character.Head.Position, head.Position}
    local ignoreList = {LocalPlayer.Character, head.Parent}
    a = workspace.CurrentCamera:GetPartsObscuringTarget(castPoints, ignoreList)
    if #a == 0 then
        return false
    end

    return true
end

function IsAlive()
    if
        LocalPlayer.Character.Humanoid.Health > 0 and LocalPlayer.Character:FindFirstChild("Humanoid") and
            LocalPlayer.Character:FindFirstChild("HumanoidRootPart")
     then
        return true
    else
        return false
    end
end

function getClosestPlayerToCursor()
    local closestPlayer

    local shortestDistance = FOV.Radius

    for i, v in pairs(game.Players:GetPlayers()) do
        if
            v ~= LocalPlayer and v.Character and v.Character:FindFirstChild("Humanoid") and
                v.Character.Humanoid.Health ~= 0 and
                v.Character:FindFirstChild("LowerTorso")
         then
            if not CheckWall(v.Character.Head) then
                local pos = CC:WorldToViewportPoint(v.Character.PrimaryPart.Position)
                local magnitude = (Vector2.new(pos.X, pos.Y) - Vector2.new(LocalMouse.X, LocalMouse.Y)).magnitude
                if magnitude < shortestDistance then
                    closestPlayer = v
                    shortestDistance = magnitude
                end
            end
        end
    end
    return closestPlayer
end

local UIS = game:GetService("UserInputService")
local RunService = game:GetService("RunService")

local VisualizerFolder = Instance.new("Folder")
VisualizerFolder.Parent = game.Workspace.Terrain

function createvisualizer()
    local Visualizer = Instance.new("Part")
    Visualizer.Anchored = true
    Visualizer.CanCollide = false
    Visualizer.Size = Vector3.new(2, 2, 2)
    Visualizer.Parent = VisualizerFolder
    Visualizer.Color = Color3.fromRGB(0, 0, 0)
    Visualizer.Shape = Enum.PartType.Ball
    if Script.Desync.Velocity.Desync and not Script.Desync.CFrame.Desync and getgenv().VisualizerVelocity ~= nil then
        Visualizer.Position = LocalPlayer.Character.HumanoidRootPart.Position + getgenv().VisualizerVelocity * 0.1413
    else
        Visualizer.CFrame = LocalPlayer.Character.HumanoidRootPart.CFrame
    end
    Visualizer.Transparency = 1
    BoxVar = Instance.new("BoxHandleAdornment", Visualizer)
    BoxVar.Name = "Box"
    BoxVar.AlwaysOnTop = true
    BoxVar.ZIndex = 4
    BoxVar.Adornee = Visualizer
    BoxVar.Color3 = Script.Desync.Velocity.VisualizeColor
    BoxVar.Transparency = 0.5
    BoxVar.Size = Visualizer.Size
    game:GetService("RunService").RenderStepped:Wait()
    Visualizer:Destroy()
end

local Window = Library:CreateWindow("osiris", Vector2.new(492, 598), Enum.KeyCode.RightShift)

--// Tabs
local Main = Window:CreateTab("Main")
local Rage = Window:CreateTab("Rage")
local Misc = Window:CreateTab("Misc")
local Visuals = Window:CreateTab("Visuals")
local Settings = Window:CreateTab("Settings")

--// Sectors
local a = Main:CreateSector("Movement", "left")
local b = Main:CreateSector("Anti Aim", "right")
local c = Misc:CreateSector("Misc", "left")
local d = Misc:CreateSector("Shit Talk", "right")
local e = Misc:CreateSector("Cursor", "right")
local f = Rage:CreateSector("Target Aim", "left")
local g = Rage:CreateSector("Part", "right")
local i = Rage:CreateSector("Tracer", "right")
local h = Visuals:CreateSector("Self Visuals", "right")
local j = Main:CreateSector("Target Strafe", "left")
local k = Rage:CreateSector("Ragebot", "left")
local l = Visuals:CreateSector("World Visuals", "right")
local n = Rage:CreateSector("Aimlock", "left")
local o = Rage:CreateSector("FOV", "right")
local p = Misc:CreateSector("Auto Buys", "left")
local q = Misc:CreateSector("Animations", "left")

local LibrarySettings = Settings:CreateSector("Settings", "left")

local Speed =
    a:AddToggle(
    "Speed",
    false,
    function(Boolean)
        Script.Main.Speed = Boolean
    end
):AddKeybind()

a:AddDropdown(
    "Method",
    {"CFrame", "BHop"},
    "CFrame",
    false,
    function(Option)
        Script.Main.SpeedType = Option

        if Option ~= "BHop" then
            LocalPlayer.Character.Humanoid.UseJumpPower = true
        end
    end
)

a:AddSlider(
    "Speed",
    0,
    1,
    100,
    1,
    function(Value)
        Script.Main.SpeedPower = Value / 40
    end
)

a:AddToggle(
    "Infinite Jump",
    false,
    function(Boolean)
        Script.Main.InfiniteJump = Boolean

        if Script.Main.InfiniteJump then
            LocalPlayer.Character.Humanoid.UseJumpPower = false
            local InfiniteJump =
                UIS.InputBegan:Connect(
                function(key)
                    if key.KeyCode == Enum.KeyCode.Space and Script.Main.InfiniteJump then
                        LocalPlayer.Character.Humanoid:ChangeState("Jumping")
                    elseif not Script.Main.InfiniteJump then
                        LocalPlayer.Character.Humanoid.UseJumpPower = true
                    end
                end
            )
        end
    end
)

a:AddToggle(
    "Fake Macro",
    false,
    function(Boolean)
        Script.Main.FakeMacro = Boolean

        if Script.Main.FakeMacro then
            local Dance = game:GetService("ReplicatedStorage").ClientAnimations.Crouching
            LoadedAnim = LocalPlayer.Character.Humanoid:LoadAnimation(Dance)
            LoadedAnim:Play()
        else
            pcall(
                function()
                    LoadedAnim:Stop()
                end
            )
        end

        while Script.Main.FakeMacro == true do
            task.wait()
            LocalPlayer.Character.HumanoidRootPart.Velocity =
                LocalPlayer.Character.HumanoidRootPart.CFrame.lookVector * 190
        end
    end
):AddKeybind()
--[[Toggle:AddColorpicker(Color3.fromRGB(255,0,0), function(Color)
    print(Color)
end)]]
a:AddLabel("Label")

b:AddSeperator("Animations")

b:AddToggle(
    "Bicycle",
    false,
    function(Boolean)
        if Boolean then
            local Dance = game:GetService("ReplicatedStorage").ClientAnimations.Bicycling
            LoadedAnim = LocalPlayer.Character.Humanoid:LoadAnimation(Dance)
            LoadedAnim:Play()
        else
            pcall(
                function()
                    LoadedAnim:Stop()
                end
            )
        end
    end
):AddKeybind()

b:AddToggle(
    "Block",
    false,
    function(Boolean)
        if Boolean then
            local Dance = game:GetService("ReplicatedStorage").ClientAnimations.Block
            LoadedAnim = LocalPlayer.Character.Humanoid:LoadAnimation(Dance)
            LoadedAnim:Play()
        else
            pcall(
                function()
                    LoadedAnim:Stop()
                end
            )
        end
    end
):AddKeybind()

b:AddToggle(
    "Lay",
    false,
    function(Boolean)
        if Boolean then
            local Dance = LayAnimation
            LoadedAnim = LocalPlayer.Character.Humanoid:LoadAnimation(Dance)
            LoadedAnim:Play()
        else
            pcall(
                function()
                    LoadedAnim:Stop()
                end
            )
        end
    end
):AddKeybind()

b:AddToggle(
    "Lean",
    false,
    function(Boolean)
        if Boolean then
            local Dance = LeanAnimation
            LoadedAnim = LocalPlayer.Character.Humanoid:LoadAnimation(Dance)
            LoadedAnim:Play()
        else
            pcall(
                function()
                    LoadedAnim:Stop()
                end
            )
        end
    end
):AddKeybind()
--

b:AddToggle(
    "Dance1Animation",
    false,
    function(Boolean)
        if Boolean then
            local Dance = Dance1Animation
            LoadedAnim = LocalPlayer.Character.Humanoid:LoadAnimation(Dance)
            LoadedAnim:Play()
        else
            pcall(
                function()
                    LoadedAnim:Stop()
                end
            )
        end
    end
):AddKeybind()

b:AddToggle(
    "Dance2Animation",
    false,
    function(Boolean)
        if Boolean then
            local Dance = Dance2Animation
            LoadedAnim = LocalPlayer.Character.Humanoid:LoadAnimation(Dance)
            LoadedAnim:Play()
        else
            pcall(
                function()
                    LoadedAnim:Stop()
                end
            )
        end
    end
):AddKeybind()

b:AddSeperator("Visuals")

b:AddToggle(
    "Jitter",
    false,
    function(Boolean)
        Script.AntiAims.JitterBot = Boolean

        if Boolean then
            LocalPlayer.Character.Humanoid.AutoRotate = false
        else
            LocalPlayer.Character.Humanoid.AutoRotate = true
        end
    end
):AddKeybind()

b:AddToggle(
    "SpinBot",
    false,
    function(Boolean)
        Script.AntiAims.SpinBot = Boolean

        if Boolean then
            LocalPlayer.Character.Humanoid.AutoRotate = false
        else
            LocalPlayer.Character.Humanoid.AutoRotate = true
        end
    end
):AddKeybind()

b:AddSlider(
    "Spinbot Speed",
    1,
    100,
    100,
    1,
    function(Value)
        Script.AntiAims.SpinBotSpeed = Value
    end
)

b:AddSeperator("Desync")

b:AddToggle(
    "Velocity Desync",
    false,
    function(Boolean)
        Script.Desync.Velocity.Desync = Boolean
    end
):AddKeybind()

b:AddToggle(
    "Visualize",
    false,
    function(Boolean)
        Script.Desync.Velocity.Visualize = Boolean
    end
):AddColorpicker(
    Color3.fromRGB(203, 9, 61),
    function(Color)
        Script.Desync.Velocity.VisualizeColor = Color
    end
)

b:AddSlider(
    "Position X",
    -50,
    0,
    50,
    1,
    function(Value)
        Script.Desync.Velocity.X = Value / 2500
    end
)

b:AddSlider(
    "Position X",
    -50,
    0,
    50,
    1,
    function(Value)
        Script.Desync.Velocity.Y = Value / 2500
    end
)

b:AddSlider(
    "Position X",
    -50,
    0,
    50,
    1,
    function(Value)
        Script.Desync.Velocity.Z = Value / 2500
    end
)

b:AddToggle(
    "Unhittable",
    false,
    function(Boolean)
        Script.Desync.Velocity.Unhittable = Boolean
    end
)

b:AddSeperator("-")

b:AddToggle(
    "CFrame Desync",
    false,
    function(Boolean)
        Script.Desync.CFrame.Desync = Boolean
    end
):AddKeybind()

b:AddToggle(
    "Random Mode",
    false,
    function(Boolean)
        Script.Desync.CFrame.RandomMode = Boolean
    end
)

b:AddSlider(
    "Power",
    0,
    0,
    50,
    1,
    function(Value)
        Script.Desync.CFrame.RandomModePower = Value
    end
)

b:AddToggle(
    "Roll",
    false,
    function(Boolean)
        Script.Desync.CFrame.Roll = Boolean
    end
)

b:AddToggle(
    "Manual",
    false,
    function(Boolean)
        Script.Desync.CFrame.Manual = Boolean
    end
)

b:AddSlider(
    "X",
    -50,
    0,
    50,
    1,
    function(Value)
        Script.Desync.CFrame.X = Value
    end
)

b:AddSlider(
    "Y",
    -50,
    0,
    50,
    1,
    function(Value)
        Script.Desync.CFrame.Y = Value
    end
)

b:AddSlider(
    "Z",
    -50,
    0,
    50,
    1,
    function(Value)
        Script.Desync.CFrame.Z = Value
    end
)

b:AddSlider(
    "Rotation X",
    -360,
    0,
    360,
    1,
    function(Value)
        Script.Desync.CFrame.RotationX = Value
    end
)

b:AddSlider(
    "Rotation Y",
    -360,
    0,
    360,
    1,
    function(Value)
        Script.Desync.CFrame.RotationY = Value
    end
)

b:AddSlider(
    "Rotation Z",
    -360,
    0,
    360,
    1,
    function(Value)
        Script.Desync.CFrame.RotationZ = Value
    end
)

--fin0

j:AddToggle(
    "Target Strafe",
    false,
    function(Boolean)
        Script.Strafe.Enabled = Boolean
    end
)

j:AddToggle(
    "Desync Strafe",
    false,
    function(Boolean)
        Script.Strafe.DesyncStrafe = Boolean

        if Script.Desync.CFrame.Desync == false and Script.Strafe.DesyncStrafe then
            LinoriaNotifs:Notify("CFrame Desync must be enabled for this to work.", 5)
        end
    end
)

j:AddToggle(
    "Strafe Visualize",
    false,
    function(Boolean)
        Script.Strafe.Visual = Boolean
    end
):AddColorpicker(
    Color3.fromRGB(255, 255, 255),
    function(color)
        Script.Strafe.VisualColor = color
    end
)

j:AddSlider(
    "Strafe Speed",
    0,
    5,
    100,
    1,
    function(Value)
        Script.Strafe.Speed = Value
    end
)

j:AddSlider(
    "Radius",
    0,
    5,
    100,
    1,
    function(Value)
        Script.Strafe.Distance = Value
    end
)

j:AddSlider(
    "Height",
    0,
    5,
    100,
    1,
    function(Value)
        Script.Strafe.Height = Value
    end
)

d:AddDropdown(
    "Shit Talk Type",
    {"Emoji", "Main", "Chinese"},
    "Main",
    false,
    function(Option)
        Script.ShitTalk.Type = Option
    end
)

d:AddSlider(
    "Delay",
    0,
    30,
    30,
    1,
    function(Value)
        Script.ShitTalk.Delay = Value
    end
)

d:AddToggle(
    "Shit talk",
    false,
    function(Boolean)
        Script.ShitTalk.Enabled = Boolean
    end
)

local TopCursorToggle =
    e:AddToggle(
    "Top",
    true,
    function(Boolean)
        game:GetService("Players").LocalPlayer.PlayerGui.MainScreenGui.Aim.Top.Visible = Boolean
    end
)

local TopCursorColor =
    TopCursorToggle:AddColorpicker(
    Color3.fromRGB(255, 255, 255),
    function(color)
        game:GetService("Players").LocalPlayer.PlayerGui.MainScreenGui.Aim.Top.BackgroundColor3 = color
    end
)

local MiddleCursorToggle =
    e:AddToggle(
    "Middle",
    true,
    function(Boolean)
        game:GetService("Players").LocalPlayer.PlayerGui.MainScreenGui.Aim.Visible = Boolean
    end
)

local MiddleCursorColor =
    MiddleCursorToggle:AddColorpicker(
    Color3.fromRGB(255, 255, 255),
    function(color)
        game:GetService("Players").LocalPlayer.PlayerGui.MainScreenGui.Aim.BackgroundColor3 = color
    end
)

local BottomCursorToggle =
    e:AddToggle(
    "Bottom",
    true,
    function(Boolean)
        game:GetService("Players").LocalPlayer.PlayerGui.MainScreenGui.Aim.Bottom.Visible = Boolean
    end
)

local BottomCursorColor =
    BottomCursorToggle:AddColorpicker(
    Color3.fromRGB(255, 255, 255),
    function(color)
        game:GetService("Players").LocalPlayer.PlayerGui.MainScreenGui.Aim.Bottom.BackgroundColor3 = color
    end
)

local LeftCursorToggle =
    e:AddToggle(
    "Left",
    true,
    function(Boolean)
        game:GetService("Players").LocalPlayer.PlayerGui.MainScreenGui.Aim.Left.Visible = Boolean
    end
)

local LeftCursorColor =
    LeftCursorToggle:AddColorpicker(
    Color3.fromRGB(255, 255, 255),
    function(color)
        game:GetService("Players").LocalPlayer.PlayerGui.MainScreenGui.Aim.Left.BackgroundColor3 = color
    end
)

local RightCursorToggle =
    e:AddToggle(
    "Right",
    true,
    function(Boolean)
        game:GetService("Players").LocalPlayer.PlayerGui.MainScreenGui.Aim.Right.Visible = Boolean
    end
)

local RightCursorColor =
    RightCursorToggle:AddColorpicker(
    Color3.fromRGB(255, 255, 255),
    function(color)
        game:GetService("Players").LocalPlayer.PlayerGui.MainScreenGui.Aim.Right.BackgroundColor3 = color
    end
)

local Spin =
    e:AddToggle(
    "Spin",
    false,
    function(Boolean)
        getgenv().SpinningCursor = Boolean
    end
)

e:AddSlider(
    "Spinning Cursor Speed",
    0,
    1,
    50,
    1,
    function(Value)
        getgenv().SpinPower = Value
    end
)

e:AddToggle(
    "Swastika",
    false,
    function(Boolean)
        Swastika.Visible = Boolean
    end
):AddColorpicker(
    Color3.fromRGB(255, 255, 255),
    function(Color)
        Swastika.TextColor3 = Color
    end
)

e:AddToggle(
    "Rainbow",
    false,
    function(Boolean)
        Script.Cursor.Rainbow = Boolean
    end
)

e:AddToggle(
    "Spinning Swastika",
    false,
    function(Boolean)
        Script.Cursor.Spin = Boolean
    end
)

e:AddSlider(
    "Swastika Spin Speed",
    0,
    1,
    5,
    1,
    function(Value)
        Script.Cursor.SpinSpeed = Value
    end
)
--// Target Aim

local Enabled =
    f:AddToggle(
    "Target Aim",
    false,
    function(Boolean)
        Script.TargetAim.Enabled = Boolean
    end
)

f:AddToggle(
    "Lock Keybind",
    false,
    function(Boolean)
        getgenv().Locking = Boolean

        if getgenv().Locking == true and Script.TargetAim.Enabled then
            getgenv().Plr = getClosestPlayerToCursor()

            local Health = getgenv().Plr.Character.Humanoid.Health

            if Script.TargetAim.LookAt then
                LocalPlayer.Character.Humanoid.AutoRotate = false
            else
                LocalPlayer.Character.Humanoid.AutoRotate = true
            end

            if Script.TargetAim.Notifications then
                LinoriaNotifs:Notify("Locked Onto: " .. getgenv().Plr.Name .. "!", 3)
            end

            if Script.Tracer.Enabled then
                Tracer.Visible = true
            end

            if Script.TargetAim.ViewTarget then
                game.Workspace.Camera.CameraSubject = getgenv().Plr.Character.Humanoid
            end

            if Script.Strafe.Enabled and not Script.Strafe.DesyncStrafe then
                if Script.Strafe.Visual then
                    StrafeVisualss.Visible = true
                    StrafeVisualss.Color = Script.Strafe.VisualColor
                    StrafeVisualss.Radius = Script.Strafe.Distance
                end

                for i = 0, 10000000, Script.Strafe.Speed do
                    task.wait()
                    if getgenv().Locking and Script.Strafe.Enabled then
                        LocalPlayer.Character.HumanoidRootPart.CFrame =
                            CFrame.new(getgenv().Plr.Character.HumanoidRootPart.Position) *
                            CFrame.Angles(0, math.rad(i), 0) *
                            CFrame.new(Script.Strafe.Distance, Script.Strafe.Height, 0)
                    end
                end
            end
        else
            game.Workspace.Camera.CameraSubject = LocalPlayer.Character.Humanoid
            LocalPlayer.Character.Humanoid.AutoRotate = true
            Tracer.Visible = false
            if getgenv().HealthNotifs then
                getgenv().HealthNotifs:Disconnect()
            end
            StrafeVisualss.Visible = false
            StrafeVisualss.Position = Vector3.new(9999, 9999, 9999)
        end
    end
):AddKeybind()

f:AddToggle(
    "Notifications",
    false,
    function(Boolean)
        Script.TargetAim.Notifications = Boolean
    end
)

f:AddToggle(
    "Knock Notifs",
    false,
    function(Boolean)
        Script.TargetAim.HitNotifs = Boolean
    end
)

f:AddTextbox(
    "Target Aim Prediction",
    nil,
    function(Text)
        Script.TargetAim.Prediction = Text
    end
)

f:AddToggle(
    "Auto Prediction",
    false,
    function(Boolean)
        Script.TargetAim.AutoPrediction = Boolean
    end
)

f:AddDropdown(
    "BodyPart",
    {
        "Head",
        "HumanoidRootPart",
        "Torso",
        "UpperTorso",
        "LowerTorso",
        "RightHand",
        "LeftLowerArm",
        "RightLowerArm",
        "RightUpperArm",
        "LeftLowerLeg",
        "LeftUpperLeg",
        "LeftFoot",
        "RightFoot",
        "RightUpperLeg",
        "RightLowerLeg"
    },
    "HumanoidRootPart",
    false,
    function(Option)
        Script.TargetAim.Part = Option
        Script.TargetAim.SelectedPart = Option
    end
)

f:AddToggle(
    "Random Body HitPart",
    false,
    function(Boolean)
        Script.TargetAim.RandomBodyPart = Boolean
    end
)

f:AddToggle(
    "Resolver",
    false,
    function(Boolean)
        Script.TargetAim.Resolver = Boolean
    end
)

f:AddToggle(
    "View Target",
    false,
    function(Boolean)
        Script.TargetAim.ViewTarget = Boolean
    end
)

f:AddToggle(
    "Look At",
    false,
    function(Boolean)
        Script.TargetAim.LookAt = Boolean
    end
)

k:AddToggle(
    "RageBot",
    false,
    function(Boolean)
        Script.RageBot.Enabled = Boolean
    end
):AddKeybind()

k:AddToggle(
    "LookAt",
    false,
    function(Boolean)
        Script.RageBot.LookAt = Boolean
    end
)

k:AddToggle(
    "Resolver",
    false,
    function(Boolean)
        Script.RageBot.Resolver = Boolean
    end
)

k:AddSlider(
    "Distance",
    0,
    50,
    200,
    1,
    function(Value)
        Script.RageBot.Distance = Value
    end
)

g:AddToggle(
    "Part Enabled",
    false,
    function(Boolean)
        Script.PartSettings.PartVisible = Boolean
    end
):AddColorpicker(
    Color3.fromRGB(255, 0, 0),
    function(Color)
        Script.PartSettings.PartColor = Color
    end
)

g:AddToggle(
    "Rainbow Part",
    false,
    function(Boolean)
        Script.PartSettings.PartRainbow = Boolean
    end
)

g:AddSlider(
    "Size",
    0,
    6,
    100,
    1,
    function(Value)
        Script.PartSettings.PartSize = Vector3.new(Value, Value, Value)
    end
)

g:AddSlider(
    "Transparency",
    0,
    1,
    10,
    1,
    function(Value)
        Script.PartSettings.PartTransparency = Value / 10
    end
)

g:AddDropdown(
    "Material",
    {"Neon", "Plastic", "ForceField"},
    "ForceField",
    false,
    function(Option)
        Script.PartSettings.PartMaterial = Enum.Material[Option]
    end
)

g:AddDropdown(
    "Shape",
    {"Cylinder", "Block", "Ball"},
    "Block",
    false,
    function(Option)
        Script.PartSettings.PartType = Enum.PartType[Option]
    end
)

l:AddToggle(
    "Bullet Tracers",
    false,
    function(Boolean)
        BulletTracers = Boolean
    end
):AddColorpicker(
    Color3.fromRGB(255, 0, 0),
    function(Color)
        BulletTracerColor = Color
    end
)

l:AddSlider(
    "Bullet Thickness",
    0,
    5,
    10,
    1,
    function(Value)
        BulletWidth = Value
    end
)

l:AddToggle(
    "Custom Gun SFX",
    false,
    function(Boolean)
        Script.Misc.CustomGunSFX = Boolean
    end
)

l:AddTextbox(
    "ID",
    nil,
    function(Text)
        Script.Misc.ID = "rbxassetid://" .. Text .. ""
    end
)

l:AddSlider(
    "Volume",
    0,
    5,
    10,
    1,
    function(Value)
        Script.Misc.Volume = Value
    end
)

local Ambient =
    l:AddToggle(
    "Ambient",
    false,
    function(Boolean)
        Ambient = Boolean

        if not Ambient then
            game:GetService("Lighting").OutdoorAmbient = Color3.fromRGB(152, 152, 146)
            game:GetService("Lighting").Ambient = Color3.fromRGB(0, 0, 0)
        end
    end
)

game:GetService("Lighting").Ambient = Color3.fromRGB(0, 0, 0)
game:GetService("Lighting").OutdoorAmbient = Color3.fromRGB(152, 152, 146)

Ambient:AddColorpicker(
    Color3.fromRGB(255, 255, 255),
    function(Color)
        if Ambient then
            game:GetService("Lighting").Ambient = Color
        end
    end
)

game:GetService("Lighting").Ambient = Color3.fromRGB(0, 0, 0)
game:GetService("Lighting").OutdoorAmbient = Color3.fromRGB(152, 152, 146)

Ambient:AddColorpicker(
    Color3.fromRGB(255, 255, 255),
    function(Color)
        if Ambient then
            game:GetService("Lighting").OutdoorAmbient = Color
        end
    end
)

game:GetService("Lighting").Ambient = Color3.fromRGB(0, 0, 0)
game:GetService("Lighting").OutdoorAmbient = Color3.fromRGB(152, 152, 146)

local highlight =
    h:AddToggle(
    "Shadow",
    false,
    function(state)
        FFBody = state

        if not FFBody then
            if LocalPlayer.Character then
                for i, v in pairs(LocalPlayer.Character:GetChildren()) do
                    if v:IsA("BasePart") then
                        v.Material = Enum.Material.Plastic
                    end
                end
            end
        end
    end
)

function Weld(x, y)
    local W = Instance.new("Weld")
    W.Part0 = x
    W.Part1 = y
    local CJ = CFrame.new(x.Position)
    local C0 = x.CFrame:inverse() * CJ
    local C1 = y.CFrame:inverse() * CJ
    W.C0 = C0
    W.C1 = C1
    W.Parent = x
end

h:AddToggle(
    "Custom Character",
    false,
    function(state)
        if state then
            for i, v in pairs(game.Players.LocalPlayer.Character:GetDescendants()) do
                if v:IsA("BasePart") or v:IsA("Decal") then
                    v.Transparency = 1
                end
            end

            getgenv().Custom =
                LocalPlayer.Character:WaitForChild("Humanoid").Died:Connect(
                function()
                    fuc:Destroy()
                    wait(5)
                    fuc = Instance.new("Part", workspace)
                    fuc.CFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame
                    fuc.CanCollide = false
                    fuck = Instance.new("SpecialMesh")
                    fuck.Parent = fuc
                    fuck.MeshType = "FileMesh"
                    if getgenv().CharacterType == "AmongUs" then
                        fuck.Scale = Vector3.new(0.2, 0.2, 0.2)
                        fuck.TextureId = "http://www.roblox.com/asset/?id=6686375937"
                        fuck.MeshId = "http://www.roblox.com/asset/?id=6686375902"
                    elseif getgenv().CharacterType == "Stewie" then
                        fuck.Scale = Vector3.new(0.1, 0.1, 0.1)
                        fuck.TextureId = "http://www.roblox.com/asset/?id=3692134820"
                        fuck.MeshId = "http://www.roblox.com/asset/?id=3692134742"
                    elseif getgenv().CharacterType == "Sonic" then
                        fuck.Scale = Vector3.new(0.1, 0.1, 0.1)
                        fuck.TextureId = "http://www.roblox.com/asset/?id=6901422268"
                        fuck.MeshId = "http://www.roblox.com/asset/?id=6901422170"
                    elseif getgenv().CharacterType == "Chicken" then
                        fuck.Scale = Vector3.new(3, 3, 3)
                        fuck.TextureId = "http://www.roblox.com/asset/?id=2114220248"
                        fuck.MeshId = "http://www.roblox.com/asset/?id=2114220154"
                    end

                    Weld(game.Players.LocalPlayer.Character.HumanoidRootPart, fuc)

                    for i, v in pairs(game.Players.LocalPlayer.Character:GetDescendants()) do
                        if v:IsA("BasePart") or v:IsA("Decal") then
                            v.Transparency = 1
                        end
                    end
                end
            )

            fuc = Instance.new("Part", workspace)
            fuc.CFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame
            fuc.CanCollide = false
            fuck = Instance.new("SpecialMesh")
            fuck.Parent = fuc
            fuck.MeshType = "FileMesh"

            if getgenv().CharacterType == "AmongUs" then
                fuck.Scale = Vector3.new(0.2, 0.2, 0.2) --sizerbxassetid://6901422268
                fuck.TextureId = "http://www.roblox.com/asset/?id=6686375937" --Texture / Skin
                fuck.MeshId = "http://www.roblox.com/asset/?id=6686375902" -- Mesh Id
            elseif getgenv().CharacterType == "Stewie" then
                fuck.Scale = Vector3.new(0.1, 0.1, 0.1) --sizerbxassetid://6901422268
                fuck.TextureId = "http://www.roblox.com/asset/?id=3692134820" --Texture / Skin
                fuck.MeshId = "http://www.roblox.com/asset/?id=3692134742" -- Mesh Id
            elseif getgenv().CharacterType == "Sonic" then
                fuck.Scale = Vector3.new(0.1, 0.1, 0.1) --sizerbxassetid://6901422268
                fuck.TextureId = "http://www.roblox.com/asset/?id=6901422268" --Texture / Skin
                fuck.MeshId = "http://www.roblox.com/asset/?id=6901422170"
            elseif getgenv().CharacterType == "Chicken" then
                fuck.Scale = Vector3.new(3, 3, 3) --sizerbxassetid://6901422268
                fuck.TextureId = "http://www.roblox.com/asset/?id=2114220248" --Texture / Skin
                fuck.MeshId = "http://www.roblox.com/asset/?id=2114220154" -- Mesh Id
            end

            Weld(game.Players.LocalPlayer.Character.HumanoidRootPart, fuc)
        else
            fuc:Destroy()

            for i, v in pairs(game.Players.LocalPlayer.Character:GetDescendants()) do
                if v:IsA("BasePart") or v:IsA("Decal") and v.Name ~= "CUFF" then
                    v.Transparency = 0
                end

                if v.Name == "CUFF" then
                    v:Destroy()
                end
            end

            for i, v in pairs(LocalPlayer.Character.BodyEffects.SpecialParts:GetDescendants()) do
                if v:IsA("BasePart") or v:IsA("Decal") then
                    v.Transparency = 1
                end
            end

            getgenv().Custom:Disconnect()

            LocalPlayer.Character.HumanoidRootPart.Transparency = 1
        end
    end
)

h:AddDropdown(
    "Character Type",
    {"AmongUs", "Stewie", "Sonic", "Chicken"},
    "AmongUs",
    false,
    function(Option)
        getgenv().CharacterType = Option

        if Option == "AmongUs" then
            fuck.Scale = Vector3.new(0.2, 0.2, 0.2) --sizerbxassetid://6901422268
            fuck.TextureId = "http://www.roblox.com/asset/?id=6686375937" --Texture / Skin
            fuck.MeshId = "http://www.roblox.com/asset/?id=6686375902" -- Mesh Id
        elseif Option == "Stewie" then
            fuck.Scale = Vector3.new(0.1, 0.1, 0.1) --sizerbxassetid://6901422268
            fuck.TextureId = "http://www.roblox.com/asset/?id=3692134820" --Texture / Skin
            fuck.MeshId = "http://www.roblox.com/asset/?id=3692134742" -- Mesh Id
        elseif Option == "Sonic" then
            fuck.Scale = Vector3.new(0.25, 0.25, 0.25) --sizerbxassetid://6901422268
            fuck.TextureId = "http://www.roblox.com/asset/?id=6901422268" --Texture / Skin
            fuck.MeshId = "http://www.roblox.com/asset/?id=6901422170"
        elseif Option == "Chicken" then
            fuck.Scale = Vector3.new(3, 3, 3) --sizerbxassetid://6901422268
            fuck.TextureId = "http://www.roblox.com/asset/?id=2114220248" --Texture / Skin
            fuck.MeshId = "http://www.roblox.com/asset/?id=2114220154" -- Mesh Id
        end
    end
)

highlight:AddColorpicker(
    Color3.fromRGB(255, 255, 255),
    function(Color)
        FFBodyColour = Color
    end
)

local skybox = Instance.new("Sky")
skybox.Parent = game.Lighting
skybox.SkyboxBk = "rbxassetid://600830446"
skybox.SkyboxDn = "rbxassetid://600831635"
skybox.SkyboxFt = "rbxassetid://600832720"
skybox.SkyboxLf = "rbxassetid://600886090"
skybox.SkyboxRt = "rbxassetid://600833862"
skybox.SkyboxUp = "rbxassetid://600835177"

l:AddToggle(
    "Custom Skyboxes",
    false,
    function(Boolean)
        getgenv().Skybox = Boolean

        if not getgenv().Skybox then
            skybox.SkyboxBk = "rbxassetid://600830446"
            skybox.SkyboxDn = "rbxassetid://600831635"
            skybox.SkyboxFt = "rbxassetid://600832720"
            skybox.SkyboxLf = "rbxassetid://600886090"
            skybox.SkyboxRt = "rbxassetid://600833862"
            skybox.SkyboxUp = "rbxassetid://600835177"
        end
    end
)

l:AddDropdown(
    "Skybox",
    {"Normal", "DoomSpire", "CatGirl", "Vibe", "Blue Aurora"},
    "Normal",
    false,
    function(Option)
        getgenv().SkyBoxOption = Option

        if getgenv().Skybox then
            if getgenv().SkyBoxOption == "DoomSpire" then
                skybox.SkyboxBk = "rbxassetid://6050664592"
                skybox.SkyboxDn = "rbxassetid://6050648475"
                skybox.SkyboxFt = "rbxassetid://6050644331"
                skybox.SkyboxLf = "rbxassetid://6050649245"
                skybox.SkyboxRt = "rbxassetid://6050649718"
                skybox.SkyboxUp = "rbxassetid://6050650083"
            elseif getgenv().SkyBoxOption == "Normal" then
                skybox.SkyboxBk = "rbxassetid://600830446"
                skybox.SkyboxDn = "rbxassetid://600831635"
                skybox.SkyboxFt = "rbxassetid://600832720"
                skybox.SkyboxLf = "rbxassetid://600886090"
                skybox.SkyboxRt = "rbxassetid://600833862"
                skybox.SkyboxUp = "rbxassetid://600835177"
            elseif getgenv().SkyBoxOption == "CatGirl" then
                skybox.SkyboxBk = "rbxassetid://444167615"
                skybox.SkyboxDn = "rbxassetid://444167615"
                skybox.SkyboxFt = "rbxassetid://444167615"
                skybox.SkyboxLf = "rbxassetid://444167615"
                skybox.SkyboxRt = "rbxassetid://444167615"
                skybox.SkyboxUp = "rbxassetid://444167615"
            elseif getgenv().SkyBoxOption == "Vibe" then
                skybox.SkyboxBk = "rbxassetid://1417494030"
                skybox.SkyboxDn = "rbxassetid://1417494146"
                skybox.SkyboxFt = "rbxassetid://1417494253"
                skybox.SkyboxLf = "rbxassetid://1417494402"
                skybox.SkyboxRt = "rbxassetid://1417494499"
                skybox.SkyboxUp = "rbxassetid://1417494643"
            elseif getgenv().SkyBoxOption == "Blue Aurora" then
                skybox.SkyboxBk = "rbxassetid://12064107"
                skybox.SkyboxDn = "rbxassetid://12064152"
                skybox.SkyboxFt = "rbxassetid://12064121"
                skybox.SkyboxLf = "rbxassetid://12063984"
                skybox.SkyboxRt = "rbxassetid://12064115"
                skybox.SkyboxUp = "rbxassetid://12064131"
            end
        end
    end
)

---

i:AddToggle(
    "Tracer",
    false,
    function(Boolean)
        Script.Tracer.Enabled = Boolean

        if Script.Tracer.Enabled == false then
            Tracer.Visible = false
        end
    end
):AddColorpicker(
    Color3.fromRGB(255, 0, 0),
    function(Color)
        Script.Tracer.Color = Color

        Tracer.Color = Script.Tracer.Color
    end
)

i:AddSlider(
    "Tracer Thickness",
    0,
    1,
    10,
    1,
    function(Value)
        Script.Tracer.Thickness = Value

        Tracer.Thickness = Script.Tracer.Thickness
    end
)

i:AddDropdown(
    "Origin",
    {"Mouse", "Character"},
    "Mouse",
    false,
    function(Option)
        Script.Tracer.Origin = Option
    end
)

c:AddToggle(
    "Auto Stomp",
    false,
    function(state)
        Script.Misc.AutoStomp = state
    end
)

c:AddToggle(
    "Auto Reload",
    false,
    function(state)
        Script.Misc.AutoReload = state
    end
)

c:AddToggle(
    "Pick-Up Monkey",
    false,
    function(state)
        Script.Misc.PickUpMoney = state
    end
)

c:AddToggle(
    "Anti Stomp",
    false,
    function(state)
        Script.Misc.AntiStomp = state
    end
)

c:AddToggle(
    "Anti Bag",
    false,
    function(state)
        Script.Misc.AntiBag = state
    end
)

c:AddToggle(
    "Jump Cooldown",
    true,
    function(state)
        LocalPlayer.Character.Humanoid.UseJumpPower = state
    end
)

----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
--------------------------------SETTINGS BELLOW-----------------------------------
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
Settings:CreateConfigSystem("right")

LibrarySettings:AddTextbox(
    "Watermark Name",
    nil,
    function(Text)
        Script.Settings.CheatName = Text
        Library:CreateWatermark("" .. Script.Settings.CheatName .. " | {fps} | {game}")
    end
)

LibrarySettings:AddToggle(
    "Watermark",
    true,
    function(Boolean)
        game:GetService("CoreGui").Watermark.Enabled = Boolean
    end
)

LibrarySettings:AddToggle(
    "No FPS Cap",
    true,
    function(Boolean)
        if Boolean then
            setfpscap(99999)
        end
    end
)

LibrarySettings:AddTextbox(
    "FPS Cap",
    nil,
    function(Text)
        setfpscap(Text)
    end
)

--[[
        Enabled = false,
        Prediction = 0.1413,
        AutoPrediction = false,
        Resolver = false

]]
n:AddToggle(
    "CamLock",
    false,
    function(state)
        Script.CamLock.Enabled = state
    end
)

n:AddToggle(
    "KeyBind",
    false,
    function(state)
        getgenv().CamLocking = state

        if getgenv().CamLocking and Script.CamLock.Enabled == true then
            getgenv().CLT = getClosestPlayerToCursor()
        end
    end
):AddKeybind()

n:AddTextbox(
    "CamLock Prediction",
    nil,
    function(Text)
        Script.CamLock.Prediction = Text
    end
)

n:AddDropdown(
    "Camlock Part",
    {"Head", "HumanoidRootPart", "UpperTorso", "LowerTorso"},
    "Head",
    false,
    function(Option)
        Script.CamLock.Part = Option
    end
)

n:AddSlider(
    "Smoothness",
    0,
    100,
    100,
    1,
    function(Value)
        Script.CamLock.Smoothness = Value / 100
    end
)

n:AddToggle(
    "Resolver",
    false,
    function(state)
        Script.CamLock.Resolver = state
    end
)

--// FOV

local fov =
    o:AddToggle(
    "FOV",
    false,
    function(state)
        FOV.Visible = state

        if FOV.Visible == false then
            FOV.Radius = math.huge
        else
            FOV.Radius = abc
        end
    end
)

fov:AddColorpicker(
    Color3.fromRGB(255, 255, 255),
    function(Color)
        FOV.Color = Color
    end
)

fov:AddKeybind()

o:AddToggle(
    "FOV Filled",
    false,
    function(state)
        FOV.Filled = state
    end
)

o:AddSlider(
    "FOV Radius",
    0,
    200,
    1000,
    1,
    function(Value)
        FOV.Radius = Value
        abc = Value
    end
)

o:AddSlider(
    "FOV Transparency",
    0,
    10,
    10,
    1,
    function(Value)
        FOV.Transparency = Value / 10
    end
)

o:AddSlider(
    "FOV Sides",
    0,
    100,
    100,
    1,
    function(Value)
        FOV.NumSides = Value
    end
)

o:AddSlider(
    "FOV Thickness",
    0,
    5,
    10,
    1,
    function(Value)
        FOV.Thickness = Value / 3.33333
    end
)

local BuysUwu =
    p:AddDropdown(
    "Other",
    Buys,
    "Pick me",
    false,
    function(Option)
        if Option then
            local OldPosition = LocalPlayer.Character.HumanoidRootPart.CFrame
            LocalPlayer.Character.HumanoidRootPart.CFrame =
                game:GetService("Workspace").Ignored.Shop[Option].Head.CFrame
            wait(0.5)
            fireclickdetector(game:GetService("Workspace").Ignored.Shop[Option].ClickDetector)
            fireclickdetector(game:GetService("Workspace").Ignored.Shop[Option].ClickDetector)
            fireclickdetector(game:GetService("Workspace").Ignored.Shop[Option].ClickDetector)
            fireclickdetector(game:GetService("Workspace").Ignored.Shop[Option].ClickDetector)
            fireclickdetector(game:GetService("Workspace").Ignored.Shop[Option].ClickDetector)
            fireclickdetector(game:GetService("Workspace").Ignored.Shop[Option].ClickDetector)
            wait(0.5)
            LocalPlayer.Character.HumanoidRootPart.CFrame = OldPosition
        end
    end
)

local BuyOptions =
    p:AddDropdown(
    "Ammo",
    Buys,
    "Ammo",
    false,
    function(Option)
        if Option then
            local OldPosition = LocalPlayer.Character.HumanoidRootPart.CFrame
            LocalPlayer.Character.HumanoidRootPart.CFrame =
                game:GetService("Workspace").Ignored.Shop[Option].Head.CFrame
            wait(0.5)
            fireclickdetector(game:GetService("Workspace").Ignored.Shop[Option].ClickDetector)
            fireclickdetector(game:GetService("Workspace").Ignored.Shop[Option].ClickDetector)
            fireclickdetector(game:GetService("Workspace").Ignored.Shop[Option].ClickDetector)
            fireclickdetector(game:GetService("Workspace").Ignored.Shop[Option].ClickDetector)
            fireclickdetector(game:GetService("Workspace").Ignored.Shop[Option].ClickDetector)
            fireclickdetector(game:GetService("Workspace").Ignored.Shop[Option].ClickDetector)
            wait(0.5)
            LocalPlayer.Character.HumanoidRootPart.CFrame = OldPosition
        end
    end
)

local Buys = {}
--[[
for i,v in pairs(game:GetService("Workspace").Ignored.Shop:GetChildren()) do 
    if v:IsA("Model") then 
        if not string.match(v.Name, "Ammo") then
            if not string.match(v.Name, "Phone") then 
                if not string.match(v.Name, "Mask") then 
                    if not string.match(v.Name, "Weights") then 
                        BuysUwu:Add(v.Name)
                    end 
                end 
            end 
        end 
    end 
end 

for i,v in pairs(game:GetService("Workspace").Ignored.Shop:GetChildren()) do 
    if v:IsA("Model") then 
        if string.match(v.Name, "Ammo") then
            BuyOptions:Add(v.Name)
        end 
    end 
end 
]]
q:AddToggle(
    "Animation Changer",
    false,
    function(state)
        Anim = state
    end
)

q:AddDropdown(
    "Idle",
    {
        "Nothing",
        "Astronaut",
        "Bubbly",
        "Cartoony",
        "Confindent",
        "Cowboy",
        "Zombie",
        "Elder",
        "Ghost",
        "Knight",
        "Levitation",
        "Mage",
        "Astronaut",
        "Ninja",
        "OldSchool",
        "Patrol",
        "Pirate",
        "Popstar",
        "Princess",
        "Robot",
        "Rthro",
        "Stylish",
        "Superhero",
        "Toy",
        "Vampire",
        "Werewolf"
    },
    "Rthro",
    false,
    function(Option)
        local ballocks = Option

        if Anim then
            while wait(3) do
                if Anim then
                    LocalPlayer.Character.Animate.idle.Animation1.AnimationId = AnimationModule[ballocks][1]
                    LocalPlayer.Character.Animate.idle.Animation2.AnimationId = AnimationModule[ballocks][2]
                end
            end
        end
    end
)

q:AddDropdown(
    "Walk",
    {
        "Nothing",
        "Astronaut",
        "Bubbly",
        "Cartoony",
        "Confindent",
        "Cowboy",
        "Zombie",
        "Elder",
        "Ghost",
        "Knight",
        "Levitation",
        "Mage",
        "Astronaut",
        "Ninja",
        "OldSchool",
        "Patrol",
        "Pirate",
        "Popstar",
        "Princess",
        "Robot",
        "Rthro",
        "Stylish",
        "Superhero",
        "Toy",
        "Vampire",
        "Werewolf"
    },
    "Rthro",
    false,
    function(Option)
        local ballockss = Option

        if Anim then
            while wait(3) do
                if Anim then
                    LocalPlayer.Character.Animate.walk.WalkAnim.AnimationId = AnimationModule[ballockss][3]
                end
            end
        end
    end
)

q:AddDropdown(
    "Run",
    {
        "Nothing",
        "Astronaut",
        "Bubbly",
        "Cartoony",
        "Confindent",
        "Cowboy",
        "Zombie",
        "Elder",
        "Ghost",
        "Knight",
        "Levitation",
        "Mage",
        "Astronaut",
        "Ninja",
        "OldSchool",
        "Patrol",
        "Pirate",
        "Popstar",
        "Princess",
        "Robot",
        "Rthro",
        "Stylish",
        "Superhero",
        "Toy",
        "Vampire",
        "Werewolf"
    },
    "Rthro",
    false,
    function(Option)
        local Run = Option

        if Anim then
            while wait(3) do
                if Anim then
                    LocalPlayer.Character.Animate.run.RunAnim.AnimationId = AnimationModule[Run][4]
                end
            end
        end
    end
)

q:AddDropdown(
    "Fall",
    {
        "Nothing",
        "Astronaut",
        "Bubbly",
        "Cartoony",
        "Confindent",
        "Cowboy",
        "Zombie",
        "Elder",
        "Ghost",
        "Knight",
        "Levitation",
        "Mage",
        "Astronaut",
        "Ninja",
        "OldSchool",
        "Patrol",
        "Pirate",
        "Popstar",
        "Princess",
        "Robot",
        "Rthro",
        "Stylish",
        "Superhero",
        "Toy",
        "Vampire",
        "Werewolf"
    },
    "Rthro",
    false,
    function(Option)
        local fall = Option

        if Anim then
            while wait(3) do
                if Anim then
                    LocalPlayer.Character.Animate.fall.FallAnim.AnimationId = AnimationModule[fall][7]
                end
            end
        end
    end
)

q:AddDropdown(
    "Jump",
    {
        "Nothing",
        "Astronaut",
        "Bubbly",
        "Cartoony",
        "Confindent",
        "Cowboy",
        "Zombie",
        "Elder",
        "Ghost",
        "Knight",
        "Levitation",
        "Mage",
        "Astronaut",
        "Ninja",
        "OldSchool",
        "Patrol",
        "Pirate",
        "Popstar",
        "Princess",
        "Robot",
        "Rthro",
        "Stylish",
        "Superhero",
        "Toy",
        "Vampire",
        "Werewolf"
    },
    "Rthro",
    false,
    function(Option)
        local pooop = Option

        if Anim then
            while wait(3) do
                if Anim then
                    LocalPlayer.Character.Animate.jump.JumpAnim.AnimationId = AnimationModule[pooop][5]
                end
            end
        end
    end
)

LPH_JIT_ULTRA(
    function()
        RunService.heartbeat:Connect(
            function()
                for _, v in pairs(LocalPlayer.Character:GetChildren()) do
                    if v:IsA("Script") and v.Name ~= "Health" and v.Name ~= "Sound" and v:FindFirstChild("LocalScript") then
                        v:Destroy()
                    end
                end

                if FOV.Visible then
                    FOV.Position = Vector2.new(LocalMouse.X, LocalMouse.Y + 36)
                end

                if getgenv().CamLocking then
                    if getgenv().CLT ~= nil then
                        local Pos, OnScreen = CC:WorldToViewportPoint(getgenv().CLT.Character.Head.Position)
                        if OnScreen and Script.CamLock.Enabled then
                            if Script.CamLock.Resolver then
                                getgenv().Main =
                                    CFrame.new(
                                    CC.CFrame.p,
                                    getgenv().CLT.Character[Script.CamLock.Part].Position +
                                        (getgenv().CLT.Character.Humanoid.MoveDirection * 3)
                                )
                                CC.CFrame =
                                    CC.CFrame:Lerp(
                                    getgenv().Main,
                                    Script.CamLock.Smoothness,
                                    Enum.EasingStyle.Elastic,
                                    Enum.EasingDirection.InOut
                                )
                            else
                                getgenv().Main =
                                    CFrame.new(
                                    CC.CFrame.p,
                                    getgenv().CLT.Character[Script.CamLock.Part].Position +
                                        (getgenv().CLT.Character.HumanoidRootPart.Velocity * Script.CamLock.Prediction)
                                )
                                CC.CFrame =
                                    CC.CFrame:Lerp(
                                    getgenv().Main,
                                    Script.CamLock.Smoothness,
                                    Enum.EasingStyle.Elastic,
                                    Enum.EasingDirection.InOut
                                )
                            end
                        end
                    end
                end

                if Script.Misc.AutoReload then
                    if game:GetService("Players").LocalPlayer.Character:FindFirstChildWhichIsA("Tool") ~= nil then
                        if
                            game:GetService("Players").LocalPlayer.Character:FindFirstChildWhichIsA("Tool"):FindFirstChild(
                                "Ammo"
                            )
                         then
                            if
                                game:GetService("Players").LocalPlayer.Character:FindFirstChildWhichIsA("Tool"):FindFirstChild(
                                    "Ammo"
                                ).Value <= 0
                             then
                                game:GetService("ReplicatedStorage").MainEvent:FireServer(
                                    "Reload",
                                    game:GetService("Players").LocalPlayer.Character:FindFirstChildWhichIsA("Tool")
                                )
                            end
                        end
                    end
                end

                if Script.Misc.CustomGunSFX then
                    for i, v in pairs(LocalPlayer.Character:GetDescendants()) do
                        if v:IsA("Sound") and v.Name == "ShootSound" then
                            v.SoundId = Script.Misc.ID
                            v.Volume = Script.Misc.Volume
                        end
                    end
                end

                if Script.Misc.PickUpMoney then
                    for __, v in pairs(game:GetService("Workspace").Ignored.Drop:GetChildren()) do
                        if v.Name == "MoneyDrop" then
                            if (v.Position - LocalPlayer.Character.HumanoidRootPart.Position).Magnitude < 25 then
                                fireclickdetector(v.ClickDetector)
                            end
                        end
                    end
                end

                if Script.Misc.AntiBag then
                    if LocalPlayer.Character:FindFirstChild("Christmas_Sock") then
                        LocalPlayer.Character["Christmas_Sock"]:Destroy()
                    end
                end

                if Script.Misc.AntiStomp then
                    if LocalPlayer.Character.Humanoid.Health < 50 then
                        for __, v in pairs(LocalPlayer.Character:GetDescendants()) do
                            if v:IsA("BasePart") then
                                v:Destroy()
                            end
                        end
                    end
                end

                if Script.Misc.AutoStomp then
                    game.ReplicatedStorage.MainEvent:FireServer("Stomp")
                end

                if Swastika.Visible then
                    CursorPath.Swastika.Position = UDim2.fromOffset(LocalMouse.X - 43, LocalMouse.Y - 39)

                    if Script.Cursor.Rainbow then
                        CursorPath.Swastika.TextColor3 = Color3.fromHSV(tick() % 6 / 6, 1, 1)
                    end

                    if Script.Cursor.Spin == true then
                        CursorPath.Swastika.Rotation = CursorPath.Swastika.Rotation + Script.Cursor.SpinSpeed
                    end
                end

                if BulletTracers then
                    local ColourSequence =
                        ColorSequence.new(
                        {
                            ColorSequenceKeypoint.new(0, BulletTracerColor),
                            ColorSequenceKeypoint.new(1, BulletTracerColor)
                        }
                    )

                    for _, v in pairs(game:GetService("Workspace").Ignored:GetDescendants()) do
                        if v.Name == "BULLET_RAYS" then
                            if 100 > (v.Position - LocalPlayer.Character.HumanoidRootPart.Position).Magnitude then
                                v.GunBeam.Texture = "http://www.roblox.com/asset/?id=9150561638"
                                v.GunBeam.Width0 = BulletWidth
                                v.GunBeam.Width1 = BulletWidth
                                v.GunBeam.Color = ColourSequence
                            end
                        end
                    end
                end

                if Script.Main.Speed then
                    if Script.Main.SpeedType == "CFrame" then
                        LocalPlayer.Character.HumanoidRootPart.CFrame =
                            LocalPlayer.Character.HumanoidRootPart.CFrame +
                            LocalPlayer.Character.Humanoid.MoveDirection * Script.Main.SpeedPower
                    elseif Script.Main.SpeedType == "BHop" then
                        LocalPlayer.Character.HumanoidRootPart.CFrame =
                            LocalPlayer.Character.HumanoidRootPart.CFrame +
                            LocalPlayer.Character.Humanoid.MoveDirection * Script.Main.SpeedPower
                        if
                            LocalPlayer.Character.Humanoid.MoveDirection.Magnitude > 0 and
                                LocalPlayer.Character.Humanoid:GetState() ~= Enum.HumanoidStateType.Freefall
                         then
                            LocalPlayer.Character.Humanoid.UseJumpPower = false
                            LocalPlayer.Character.Humanoid:ChangeState("Jumping")
                        end
                    end
                end

                if Script.RageBot.Enabled then
                    if game:GetService("Players").LocalPlayer.Character:FindFirstChildWhichIsA("Tool") ~= nil then
                        if
                            game:GetService("Players").LocalPlayer.Character:FindFirstChildWhichIsA("Tool"):FindFirstChild(
                                "Ammo"
                            )
                         then
                            if
                                game:GetService("Players").LocalPlayer.Character:FindFirstChildWhichIsA("Tool"):FindFirstChild(
                                    "Ammo"
                                ).Value <= 0
                             then
                                game:GetService("ReplicatedStorage").MainEvent:FireServer(
                                    "Reload",
                                    game:GetService("Players").LocalPlayer.Character:FindFirstChildWhichIsA("Tool")
                                )
                            end
                        end
                    end

                    for _, q in pairs(game:GetService("Players"):GetPlayers()) do
                        if q ~= LocalPlayer and q and q.Character then
                            local RageBotD =
                                (LocalPlayer.Character.HumanoidRootPart.Position - q.Character.HumanoidRootPart.Position).Magnitude
                            if Script.RageBot.Distance > RageBotD and not CheckWall(q.Character.Head) then
                                if q.Character.BodyEffects["K.O"].Value == false then
                                    getgenv().RBTarget = q

                                    if getgenv().RBTarget ~= nil then
                                        LocalPlayer.Character:FindFirstChildOfClass("Tool"):Activate()
                                    end
                                end
                            end
                        end
                    end
                end

                --[[if getgenv().RBTarget ~= nil and LocalPlayer.Character:FindFirstChildWhichIsA("Tool") ~= nil then  
    if LocalPlayer.Information.Armory[tostring(LocalPlayer.Character:FindFirstChildWhichIsA("Tool"))].Ammo.Normal.Value > 0 and getgenv().RBTarget ~= nil then 
    if getgenv().RBTarget ~= nil then 
    LocalPlayer.Character:FindFirstChildOfClass("Tool"):Activate()
end 
end ]]
                if Script.RageBot.LookAt and getgenv().RBTarget ~= nil then
                    local OldCframe = LocalPlayer.Character.PrimaryPart
                    local NearestRoot = getgenv().RBTarget.Character.HumanoidRootPart
                    local NearestPos =
                        CFrame.new(
                        LocalPlayer.Character.PrimaryPart.Position,
                        Vector3.new(NearestRoot.Position.X, OldCframe.Position.Y, NearestRoot.Position.Z)
                    )
                    LocalPlayer.Character:SetPrimaryPartCFrame(NearestPos)
                    LocalPlayer.Character.Humanoid.AutoRotate = false
                end

                if getgenv().SpinningCursor then
                    LocalPlayer.PlayerGui.MainScreenGui.Aim.Rotation =
                        LocalPlayer.PlayerGui.MainScreenGui.Aim.Rotation + getgenv().SpinPower
                end

                if FFBody then
                    if LocalPlayer.Character then
                        for i, v in pairs(LocalPlayer.Character:GetChildren()) do
                            if v:IsA("BasePart") then
                                v.Material = Enum.Material.ForceField
                                v.Color = FFBodyColour
                            end
                        end
                    end
                end

                if Script.AntiAims.SpinBot and not Script.AntiAims.JitterBot then
                    LocalPlayer.Character.HumanoidRootPart.CFrame =
                        LocalPlayer.Character.HumanoidRootPart.CFrame *
                        CFrame.Angles(0, Script.AntiAims.SpinBotSpeed * 0.01234, 0)
                end

                if Script.AntiAims.JitterBot and not Script.AntiAims.SpinBot then
                    local RandomJit = math.random(30, 90)
                    LocalPlayer.Character.HumanoidRootPart.CFrame =
                        CFrame.new(LocalPlayer.Character.HumanoidRootPart.CFrame.Position) *
                        CFrame.Angles(
                            0,
                            math.rad(180) + math.rad((math.random(1, 2) == 1 and RandomJit or -RandomJit)),
                            0
                        )
                end

                if Script.Desync.Velocity.Desync then
                    local lvle = LocalPlayer.Character.HumanoidRootPart.Velocity
                    local lcf = LocalPlayer.Character.HumanoidRootPart.CFrame

                    LocalPlayer.Character.HumanoidRootPart.CFrame =
                        lcf * CFrame.Angles(0, math.rad(Script.Desync.Velocity.DesyncSpinPower * 10), 0)

                    if not Script.Desync.Velocity.Unhittable then
                        LocalPlayer.Character.HumanoidRootPart.Velocity =
                            Vector3.new(Script.Desync.Velocity.X, Script.Desync.Velocity.Y, Script.Desync.Velocity.Z) *
                            -(2 ^ Script.Desync.Velocity.DesyncPower)
                    else
                        LocalPlayer.Character.HumanoidRootPart.Velocity = Vector3.new(1, 1, 1) * -(2 ^ 16)
                    end

                    RunService.RenderStepped:Wait()

                    getgenv().VisualizerVelocity = LocalPlayer.Character.HumanoidRootPart.Velocity

                    LocalPlayer.Character.HumanoidRootPart.Velocity = lvle
                end

                if getgenv().Locking then
                    if Script.TargetAim.AutoPrediction then
                        local pingvalue = game:GetService("Stats").Network.ServerStatsItem["Data Ping"]:GetValueString()
                        local split = string.split(pingvalue, "(")
                        local ping = tonumber(split[1])
                        if ping < 130 then
                            Script.TargetAim.Prediction = 0.151
                        elseif ping < 125 then
                            Script.TargetAim.Prediction = 0.149
                        elseif ping < 110 then
                            Script.TargetAim.Prediction = 0.146
                        elseif ping < 105 then
                            Script.TargetAim.Prediction = 0.138
                        elseif ping < 90 then
                            Script.TargetAim.Prediction = 0.136
                        elseif ping < 80 then
                            Script.TargetAim.Prediction = 0.134379
                        elseif ping < 70 then
                            Script.TargetAim.Prediction = 0.129762
                        elseif ping < 60 then
                            Script.TargetAim.Prediction = 0.1248976
                        elseif ping < 50 then
                            Script.TargetAim.Prediction = 0.1245
                        elseif ping < 40 then
                            Script.TargetAim.Prediction = 0.13232
                        end
                    end

                    if Script.Strafe.Enabled then
                        if Script.Strafe.Visual then
                            StrafeVisualss.Position = getgenv().Plr.Character.HumanoidRootPart.Position
                        end
                    end

                    if Script.PartSettings.PartVisible then
                        TargetPart.Color = Script.PartSettings.PartColor
                        TargetPart.CanCollide = false
                        TargetPart.Size = Script.PartSettings.PartSize
                        TargetPart.Transparency = Script.PartSettings.PartTransparency
                        TargetPart.Material = Script.PartSettings.PartMaterial
                        TargetPart.Shape = Script.PartSettings.PartType

                        TargetPart.CFrame = getgenv().Plr.Character.HumanoidRootPart.CFrame

                        if Script.PartSettings.PartRainbow then
                            TargetPart.Color = Color3.fromHSV(tick() % 6 / 6, 1, 1)
                        end
                    end

                    if Script.Tracer.Enabled then
                        local Vector = CC:WorldToViewportPoint(getgenv().Plr.Character.HumanoidRootPart.Position)
                        local LocalPlayerVector =
                            CC:WorldToViewportPoint(LocalPlayer.Character.HumanoidRootPart.Position)
                        local Inset = game:GetService("GuiService"):GetGuiInset().Y

                        if Script.Tracer.Origin == "Mouse" then
                            Tracer.From = Vector2.new(LocalMouse.X, LocalMouse.Y + Inset)
                            Tracer.To = Vector2.new(Vector.X, Vector.Y)
                        elseif Script.Tracer.Origin == "Character" then
                            Tracer.From = Vector2.new(LocalPlayerVector.X, LocalPlayerVector.Y)
                            Tracer.To = Vector2.new(Vector.X, Vector.Y)
                        end
                    end

                    if Script.TargetAim.LookAt then
                        local OldCframe = LocalPlayer.Character.PrimaryPart
                        local NearestRoot = Plr.Character.HumanoidRootPart
                        local NearestPos =
                            CFrame.new(
                            LocalPlayer.Character.PrimaryPart.Position,
                            Vector3.new(NearestRoot.Position.X, OldCframe.Position.Y, NearestRoot.Position.Z)
                        )
                        LocalPlayer.Character:SetPrimaryPartCFrame(NearestPos)
                    end

                    if Script.TargetAim.RandomBodyPart then
                        Script.TargetAim.Part = BodyParts[math.random(0, #BodyParts)]
                    end

                    if Script.SilentAim.RandomBodyPart then
                        Script.SilentAim.Part = BodyParts[math.random(0, #BodyParts)]
                    end
                else
                    -- finopa was here
                    TargetPart.CFrame = CFrame.new(9999, 9999, 9999)
                end

                if Script.Desync.Velocity.Visualize then
                    createvisualizer()
                end
            end
        )

        RunService.heartbeat:Connect(
            function()
                if Script.Main.Speed and Script.Desync.CFrame.Desync then
                    if Script.Main.SpeedType == "CFrame" then
                        LocalPlayer.Character.HumanoidRootPart.CFrame =
                            LocalPlayer.Character.HumanoidRootPart.CFrame +
                            LocalPlayer.Character.Humanoid.MoveDirection * Script.Main.SpeedPower
                    elseif Script.Main.SpeedType == "BHop" then
                        LocalPlayer.Character.HumanoidRootPart.CFrame =
                            LocalPlayer.Character.HumanoidRootPart.CFrame +
                            LocalPlayer.Character.Humanoid.MoveDirection * Script.Main.SpeedPower
                        if
                            LocalPlayer.Character.Humanoid.MoveDirection.Magnitude > 0 and
                                LocalPlayer.Character.Humanoid:GetState() ~= Enum.HumanoidStateType.Freefall
                         then
                            LocalPlayer.Character.Humanoid.UseJumpPower = false
                            LocalPlayer.Character.Humanoid:ChangeState("Jumping")
                        end
                    end
                end

                if Script.Desync.CFrame.Desync then
                    getgenv().hrppos = LocalPlayer.Character.HumanoidRootPart.CFrame

                    if Script.Desync.CFrame.RandomMode then
                        local TargetPos = LocalPlayer.Character.HumanoidRootPart.Position
                        LocalPlayer.Character.HumanoidRootPart.CFrame =
                            (CFrame.new(TargetPos) +
                            Vector3.new(
                                math.random(-Script.Desync.CFrame.RandomModePower, Script.Desync.CFrame.RandomModePower),
                                math.random(-Script.Desync.CFrame.RandomModePower, Script.Desync.CFrame.RandomModePower),
                                math.random(-Script.Desync.CFrame.RandomModePower, Script.Desync.CFrame.RandomModePower)
                            )) *
                            CFrame.Angles(
                                math.rad(math.random(-180, 180)),
                                math.rad(math.random(-180, 180)),
                                math.rad(math.random(-180, 180))
                            )
                    end

                    if Script.Strafe.DesyncStrafe and getgenv().Locking then
                        LocalPlayer.Character.HumanoidRootPart.CFrame =
                            getgenv().Plr.Character.HumanoidRootPart.CFrame * CFrame.new(0, -8, 0)
                    end

                    if Script.Desync.CFrame.Manual then
                        local Position = LocalPlayer.Character.HumanoidRootPart.Position
                        LocalPlayer.Character.HumanoidRootPart.CFrame =
                            (CFrame.new(Position) +
                            Vector3.new(Script.Desync.CFrame.X, Script.Desync.CFrame.Y, Script.Desync.CFrame.Z)) *
                            CFrame.Angles(
                                Script.Desync.CFrame.RotationX,
                                Script.Desync.CFrame.RotationY,
                                Script.Desync.CFrame.RotationZ
                            )
                    end

                    if Script.Desync.CFrame.Roll then
                        local Position = LocalPlayer.Character.HumanoidRootPart.Position
                        LocalPlayer.Character.HumanoidRootPart.CFrame =
                            (CFrame.new(Position) - Vector3.new(0, -2, 0)) * CFrame.Angles(0, 0, 5)
                    end

                    game:GetService("RunService").RenderStepped:Wait()

                    LocalPlayer.Character.HumanoidRootPart.CFrame = getgenv().hrppos

                    getgenv().hrppos = LocalPlayer.Character.HumanoidRootPart.CFrame
                end
            end
        )
    end
)()

LPH_JIT_ULTRA(
    function()
        local oldIndex
        oldIndex =
            hookmetamethod(
            game,
            "__index",
            newcclosure(
                function(self, key)
                    if not checkcaller() then
                        if
                            key == "CFrame" and Script.Desync.CFrame.Desync and LocalPlayer.Character and
                                LocalPlayer.Character:FindFirstChild("HumanoidRootPart") and
                                LocalPlayer.Character:FindFirstChild("Humanoid") and
                                LocalPlayer.Character:FindFirstChild("Humanoid").Health > 0
                         then
                            if self == LocalPlayer.Character.HumanoidRootPart then
                                return getgenv().hrppos
                            end
                        end
                    end
                    return oldIndex(self, key)
                end
            )
        )

        local rawmetatable = getrawmetatable(game)
        local old = rawmetatable.__namecall
        setreadonly(rawmetatable, false)
        rawmetatable.__namecall =
            newcclosure(
            function(...)
                local args = {...}
                if
                    getgenv().Locking and getnamecallmethod() == "FireServer" and args[2] == "UpdateMousePos" and
                        getgenv().Plr ~= nil and
                        not Script.RageBot.Enabled
                 then
                    if Script.TargetAim.Resolver == false then
                        args[3] =
                            getgenv().Plr.Character[Script.TargetAim.Part].Position +
                            (getgenv().Plr.Character[Script.TargetAim.Part].Velocity * Script.TargetAim.Prediction)
                    else
                        args[3] =
                            getgenv().Plr.Character[Script.TargetAim.Part].Position +
                            (getgenv().Plr.Character.Humanoid.MoveDirection * 3)
                    end
                    return old(unpack(args))
                end
                return old(...)
            end
        )

        local rawmetatable = getrawmetatable(game)
        local old = rawmetatable.__namecall
        setreadonly(rawmetatable, false)
        rawmetatable.__namecall =
            newcclosure(
            function(...)
                local args = {...}
                if
                    Script.RageBot.Enabled and getnamecallmethod() == "FireServer" and args[2] == "UpdateMousePos" and
                        getgenv().RBTarget ~= nil
                 then
                    if Script.RageBot.Resolver == false then
                        args[3] =
                            getgenv().RBTarget.Character[Script.TargetAim.Part].Position +
                            (getgenv().RBTarget.Character[Script.TargetAim.Part].Velocity * Script.TargetAim.Prediction)
                    else
                        args[3] =
                            getgenv().RBTarget.Character[Script.TargetAim.Part].Position +
                            (getgenv().RBTarget.Character.Humanoid.MoveDirection * 3)
                    end
                    return old(unpack(args))
                end
                return old(...)
            end
        )
    end
)()
--game:GetService("CoreGui").Watermark.Enabled = false