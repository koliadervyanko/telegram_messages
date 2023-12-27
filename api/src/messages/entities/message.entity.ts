import { GroupEntity } from 'src/group/entities/group.entity';
import { KeyWordEntity } from 'src/key-word/entities/key-word.entity';
import { Column, Entity, ManyToOne, PrimaryGeneratedColumn } from 'typeorm';
import { StringOrNull } from '../types/types';

@Entity()
export class MessageEntity {
  @PrimaryGeneratedColumn()
  id: number;
  @ManyToOne(() => GroupEntity, (group) => group.messages)
  group: GroupEntity;

  @ManyToOne(() => KeyWordEntity, (keyWord) => keyWord.messages)
  keyWord: KeyWordEntity;

  @Column()
  comment: string;

  @Column({ nullable: true })
  username: StringOrNull;

  @Column({ nullable: true })
  name: StringOrNull;

  @Column()
  date: string;

  @Column()
  hasReplies: boolean;
}
