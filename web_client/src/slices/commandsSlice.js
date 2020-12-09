import {createAsyncThunk, createSlice} from '@reduxjs/toolkit'
import {getCommands} from "../api"


export const fetchCommands = createAsyncThunk('commands/fetchCommands', async () => {
    const response = await getCommands()

    return response.data
})

const initialState = {
    commands: [],
    status: 'idle',
    error: null
}

const commandsSlice = createSlice({
    name: 'commands',
    initialState: initialState,
    reducers: {},
    extraReducers: {
        [fetchCommands.pending]: (state, action) => {
            state.status = 'loading'
        },
        [fetchCommands.fulfilled]: (state, action) => {
            state.status = 'succeeded'
            state.commands = action.payload
        },
        [fetchCommands.rejected]: (state, action) => {
            state.status = 'failed'
            state.error = action.error.message
        }
    }
})

export const selectAllCommands = (state) => state.commands.commands

export const {} = commandsSlice.actions

export default commandsSlice.reducer