import { GroupEntity } from 'src/group/entities/group.entity'
import { Column, Entity, OneToOne, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class LocationEntity {
  @PrimaryGeneratedColumn()
  id: number;
  @Column()
  country: string;
  @Column()
  city: string;

  @OneToOne(() => GroupEntity, (group) => group.location)
  group: GroupEntity
}
