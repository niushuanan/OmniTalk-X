import { persist } from 'zustand/middleware';
import { create } from 'zustand';
import { SERIAL_MODE } from '@constants/models.ts';

export interface configStore {
    token: string;
    username: string;
    mode: string;
    updateMode: (mode: string) => void;
}
export const useConfigStore = create<configStore>()(
    persist(
        (set, get) => ({
            token: '',
            username: 'user',
            mode: SERIAL_MODE, // 'parallel' | 'serial'
            updateMode: (mode: string) => {
                set({ mode });
            },
        }),
        {
            name: 'config',
        }
    ),
);
