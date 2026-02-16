import { create } from 'zustand';
import { persist } from 'zustand/middleware';

export interface GroupInfo {
    id: string;
    name: string;
    bots: string[];
    bot_names: string[];
    bot_count: number;
    is_default: boolean;
    created_at: string;
}

interface GroupStore {
    groups: GroupInfo[];
    currentGroupId: string;
    setGroups: (groups: GroupInfo[]) => void;
    setCurrentGroupId: (groupId: string) => void;
    getCurrentGroup: () => GroupInfo | undefined;
    getGroupBots: () => string[];
}

export const useGroupStore = create<GroupStore>()(
    persist(
        (set, get) => ({
            groups: [],
            currentGroupId: 'grp_all',
            
            setGroups: (groups: GroupInfo[]) => {
                set({ groups });
                if (!groups.find(g => g.id === get().currentGroupId)) {
                    const defaultGroup = groups.find(g => g.is_default);
                    if (defaultGroup) {
                        set({ currentGroupId: defaultGroup.id });
                    }
                }
            },
            
            setCurrentGroupId: (groupId: string) => {
                set({ currentGroupId: groupId });
            },
            
            getCurrentGroup: () => {
                const { groups, currentGroupId } = get();
                return groups.find(g => g.id === currentGroupId);
            },
            
            getGroupBots: () => {
                const group = get().getCurrentGroup();
                return group?.bots || [];
            }
        }),
        {
            name: 'group',
        }
    )
);
