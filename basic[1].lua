--[[ Imported c++ Functions ]]--
--initialise()
--keypress( XK_keycode )
--keydown( XK_keycode )
--keyup( XK_keycode )
--buttonpress( n )
--buttondown( n )
--buttonup( n )
--mousemove( x, y )
--mousepos( x, y )
--midi_send( { status, data1, data2 } )
--exec( 'command' )
--
--[[ Imported Global Variables ]]--
--wm_class
--autoconnect
--
--[[ Functions you must create ]]
--midi_recv( status, data1, data2 )
--loop()

------------------------

--[[ Simple Example ]]--

--[[ Defines ]]--
--play = {0x90, 0x0B, 127}

local handle = io.popen("xdotool search ".."move_circle")
local winid = math.floor(handle:read("*a"))
handle:close()

controller = {
    deck = {
        A = {
            play = {144.0} --Note on, MIDI Channel 1
        };
        F2 = {
            play = {41.0} --Note F2
        };
        F_2 = {
            play = {42.0} --Note F#2
        };
        G2 = {
            play = {43.0} --Note G2
        };
        G_2 = {
            play = {44.0} --Note G#2
        };
        
        
        
        
        
        F3 = {
            play = {53.0} --Note F3
        };
        F_3 = {
            play = {54.0} --Note F#3
        };
    }
}



--[[ global settings ]]--
-- autoconnect: can be true, false, or a named jack port. default = true
autoconnect = false

--[[ Pattern matcher for messages ]]--
--
-- Both pattern and message share the same structure: {status, data1, data2}.
-- For any element of the pattern is equal -1, corresponding element of the
-- message is ignored / considered equal. Third element is often used for
-- continuous measurements such as acceleration, thus in addition to being -1,
-- it can also be nil, i.e. omitted entirely, making it for a table of two
-- elements, like this: {0xb0, 0x15} instead of this: {0xb0, 0x15, -1}.
function message_matches( pattern, message )
    if pattern[1] ~= -1 then
        if pattern[1] ~= message[1] then return false end
    end
    if pattern[2] ~= -1 then
        if pattern[2] ~= message[2] then return false end
    end
    if pattern[3] ~= nil and pattern[3] ~= -1 then
        if pattern[3] ~= message[3] then return false end
    end
    return true
end

--[[ initialisation function ]]--
-- run immediately after the application launches and connects to the device
function script_init()
    print( "nothing to initialise" )
end

function loop()
    detectwindow()
end


--[[ Input Event Handler ]]--
function midi_recv(data1,data2)
    local status = { data1 }
    local note = { data2 }
    print(data1)
    print(data2)
    if( message_matches ( controller.deck['A'].play, status ) ) then
        --Write data1 & data2 to Log-File
        os.execute("/home/pi/m2i/log.sh "..data1.." "..data2 )
        
        --Execute Button presses for every note
        if( message_matches( controller.deck['F2'].play, note ) ) then
            os.execute("xdotool key --window "..winid.." 2+f")
           
        end
        if( message_matches( controller.deck['F_2'].play, note ) ) then
            os.execute("xdotool key --window "..winid.." 2+v")

        end
        if( message_matches( controller.deck['F3'].play, note ) ) then
            os.execute("xdotool key --window "..winid.." 3+f")
            
        end
        if( message_matches( controller.deck['F_3'].play, note ) ) then
            os.execute("xdotool key --window "..winid.." 3+v")


        end
        
    end
end
