import { Injectable, InternalServerErrorException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { GroupEntity } from './entities/group.entity';
import { Repository } from 'typeorm';
import { CreateGroupDto } from './dto/create-group.dto';
import { LocationService } from 'src/location/location.service';

@Injectable()
export class GroupService {
  constructor(
    @InjectRepository(GroupEntity) private repository: Repository<GroupEntity>,
    private locationService: LocationService,
  ) {}
  findAll() {
    try {
      return this.repository.find();
    } catch (error) {
      throw new InternalServerErrorException(`Error ${error}`);
    }
  }
  async findOne(link: string) {
    try {
      const group = await this.repository.findOneBy({ link });
      return group;
    } catch (error) {
      throw new InternalServerErrorException(`Error ${error}`);
    }
  }
  async createGroup(createGroupDto: CreateGroupDto) {
    try {
      const location = await this.locationService.findOne(
        createGroupDto.location,
      );
      return await this.repository.save({
        link: createGroupDto.link,
        location,
      });
    } catch (error) {
      throw new InternalServerErrorException(`Error ${error}`);
    }
  }
}
